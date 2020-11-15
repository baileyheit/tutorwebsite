from flask import render_template, flash, redirect,  url_for, request
from app import app, db
import uuid
from app.forms import LoginForm, RegistrationForm, EditProfileForm,  ResetPasswordRequestForm, ResetPasswordForm, AddSessionForm
from flask_login import logout_user, login_required, current_user, login_user
from app.models import User, Session, Course, Cart
from werkzeug.urls import url_parse
from datetime import datetime, date
from app.myemail import send_password_reset_email
# from flask_sqlalchemy import SQLAlchemy
# import psycopg2

# conn = psycopg2.connect()
# cur = conn.cursor()

@app.route('/')
@app.route('/index')
@login_required
def index():
    tutors = User.query.order_by(User.rating.desc(), User.grade, User.hourly_rate).limit(10).from_self()
    # tutors = User.query.join(Session, User.id==Session.tutor).order_by(User.rating.desc(), User.hourly_rate).limit(10).from_self()
    return render_template('index.html', title='Home', tutors=tutors)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        # user = User.query.filter_by(username=form.username.data).first()
        User = User.query.filter_by(username=form.username.data).first()
        if User is None or not User.check_password(form.password.data):
        # if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        # login_user(user, remember=form.remember_me.data)
        login_user(User, remember=form.remember_me.data)
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
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
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
        sessions = Session.query.join(User, Session.tutor == User.id).add_columns(
            User.username, Session.session_id, Session.subject, Session.class_num, Session.price, 
            Session.booked, Session.tutor, Session.date, Session.time, User.name).filter(
                Session.booked==0, Session.subject==subject, Session.tutor!=user_id).order_by(Session.price.asc())
    else:
        sessions = Session.query.join(User, Session.tutor == User.id).add_columns(
            User.username, Session.session_id, Session.subject, Session.class_num, Session.price, 
            Session.booked, Session.tutor, Session.date, Session.time, User.name).filter(
                Session.booked==0, Session.tutor!=user_id).order_by(Session.price.asc())
    
    cartItems = Cart.query.filter(Cart.id==user_id)

    return render_template('search.html', title='Search', sessions = sessions, cartItems=cartItems, user_id=user_id)


@app.route('/add_to_cart/<session_id>', methods=['GET', 'POST'])
@login_required
def add_to_cart(session_id):
    user_id = current_user.id
    cart_id = uuid.uuid4().int & (1<<32)-1
    cartItem = Cart(cart_id=cart_id, session_id=session_id, id=user_id)

    db.session.add(cartItem)
    db.session.commit()

    return redirect(url_for('search'))

@app.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
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
    user = User.verify_reset_password_token(token)
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
    sessions = Session.query.filter((Session.tutor==user_id) | (Session.tutee==user_id))
    return render_template('sessions.html', title='My Sessions', sessions = sessions)
    
@app.route('/cart', methods=['GET', 'POST'])
@login_required
def cart():
    user_id = current_user.id
    session_ids = [c.session_id for c in Cart.query.filter(id==user_id)]
    sessions = Session.query.filter(Session.session_id in session_ids)
    return render_template('cart.html', title='My Sessions', sessions = sessions)

@app.route('/add_session', methods=['GET', 'POST'])
@login_required
def add_session():
    form = AddSessionForm()
    if form.validate_on_submit():
        session = Session(zoom_link=form.zoom_link.data, date=form.date.data.strftime("%m/%d/%Y"), time=form.time.data.strftime("%H:%M"), price=form.price.data, tutor=current_user.id, subject=form.subject.data, class_number=form.class_number.data)
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
    return render_template('add_session.html', title='Add Session', form=form)
