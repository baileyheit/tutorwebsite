import uuid
from flask import render_template, flash, redirect,  url_for, request
from app import app, db

import uuid
from app.forms import LoginForm, RegistrationForm, EditProfileForm,  ResetPasswordRequestForm, ResetPasswordForm, AddSessionForm, AddReviewForm
from flask_login import logout_user, login_required, current_user, login_user
from app.models import user, session, course, cart, rating
from werkzeug.urls import url_parse
from datetime import datetime, date
from app.myemail import send_password_reset_email
from dateutil.parser import parse
# from flask_sqlalchemy import SQLAlchemy
# import psycopg2

# conn = psycopg2.connect()
# cur = conn.cursor()

@app.route('/')
@app.route('/index')
@login_required
def index():
    tutors = user.query.order_by(user.rating.desc(), user.grade, user.hourly_rate).limit(10).from_self()
    # tutors = user.query.join(session, user.id==session.tutor).order_by(user.rating.desc(), user.hourly_rate).limit(10).from_self()
    return render_template('index.html', title='Home', tutors=tutors)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        u = user.query.filter_by(username=form.username.data).first()
        if u is None or not u.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = user(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/user/<username>')
@login_required
def user(username):
    user = user.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile',
                           form=form)


@app.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    user_id = current_user.id
    subject = request.args.get('subject')

    if subject:
        sessions = session.query.join(user, session.tutor == user.id).add_columns(
            user.username, session.session_id, session.subject, session.class_num, session.price, 
            session.booked, session.tutor, session.date, session.time, user.name).filter(
                session.booked==0, session.subject==subject, session.tutor!=user_id).order_by(session.price.asc())
    else:
        sessions = session.query.join(user, session.tutor == user.id).add_columns(
            user.username, session.session_id, session.subject, session.class_num, session.price, 
            session.booked, session.tutor, session.date, session.time, user.name).filter(
                session.booked==0, session.tutor!=user_id).order_by(session.price.asc())
    
    cartItems = cart.query.filter(cart.id==user_id)

    return render_template('search.html', title='Search', sessions = sessions, cartItems=cartItems, user_id=user_id)


@app.route('/add_to_cart/<session_id>', methods=['GET', 'POST'])
@login_required
def add_to_cart(session_id):
    user_id = current_user.id
    cart_id = uuid.uuid4().int & (1<<32)-1
    cartItem = cart(cart_id=cart_id, session_id=session_id, id=user_id)

    db.session.add(cartItem)
    db.session.commit()

    return redirect(url_for('search'))

@app.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = user.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash('Check your email for the instructions to reset your password')
        return redirect(url_for('login'))
    return render_template('reset_password_request.html',
                           title='Reset Password', form=form)


@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    user = user.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset.')
        return redirect(url_for('login'))
    return render_template('reset_password.html', form=form)
    
@app.route('/my_sessions', methods=['GET', 'POST'])
@login_required
def my_sessions():
    user_id = current_user.id
    sessions = session.query.filter((session.tutor==user_id) | (session.tutee==user_id))
    return render_template('sessions.html', title='My sessions', sessions = sessions)
    
@app.route('/cart', methods=['GET', 'POST'])
@login_required
def cart():
    user_id = current_user.id
    session_ids = [c.session_id for c in cart.query.filter(id==user_id)]
    sessions = session.query.filter(session.session_id in session_ids)
    return render_template('cart.html', title='My sessions', sessions = sessions)

@app.route('/add_review', methods=['GET', 'POST'])
@login_required
def add_review():
    form = AddReviewForm()
    if form.validate_on_submit():
        rating = rating(rating_id = uuid.uuid4().int & (1<<32)-1 & (1<<32)-1, tutor=form.tutor.data, tutee=current_user.id, session=form.session.data, subject=form.subject.data, class_num=form.class_num.data, comment=form.class_num.data, rating_num=form.rating_num.data)
        db.session.add(rating)
        flash('Congratulations, you have now added a session!')
        db.session.commit()
        return redirect(url_for('my_sessions'))
    return render_template('add_review.html', title='Add Review', form = form)

@app.route('/add_session', methods=['GET', 'POST'])
@login_required
def add_session():
    form = AddsessionForm()
    if form.validate_on_submit():
        session = session(zoom_link=form.zoom_link.data, date=form.date.data.strftime("%m/%d/%Y"), time=form.time.data.strftime("%H:%M"), price=form.price.data, tutor=current_user.id, subject=form.subject.data, class_num=form.class_number.data)
        course = Course(subject=form.subject.data, class_num=form.class_number.data, class_name=form.class_name.data)
        db.session.add(session)
        flash('Congratulations, you have now added a session!')
        if current_user.hourly_rate:
            current_user.hourly_rate = (current_user.hourly_rate + form.price.data)/2
        else:
            current_user.hourly_rate = form.price.data
        if Course.query.filter_by(subject=form.subject.data, class_num=form.class_number.data):
            db.session.add(course)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_session.html', title='Add session', form=form)
