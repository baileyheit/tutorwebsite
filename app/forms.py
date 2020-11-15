from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, DateField, TimeField, FloatField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import user

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In') 

class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        u = user.query.filter_by(username=username.data).first()
        if u is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        u = user.query.filter_by(email=email.data).first()
        if u is not None:
            raise ValidationError('Please use a different email address.')

class EditProfileForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    name = StringField('Name', validators=[DataRequired()])
    phone_number = IntegerField('Phone Number')
    school = StringField('School')
    venmo = StringField('Venmo')
    grade = StringField('Grade')
    hourly_rate = StringField('Hourly Rate')
    submit = SubmitField('Submit')
    
    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            u = user.query.filter_by(username=self.username.data).first()
            if u is not None:
                raise ValidationError('Please use a different username.')

class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')

class AddSessionForm(FlaskForm):
    date = DateField('Day (YYYY-MM-DD)', validators=[DataRequired()])
    time = TimeField('Time (H:M)', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
    subject = StringField('Subject', validators=[DataRequired()])
    class_number = IntegerField('Class Number', validators=[DataRequired()])
    class_name = StringField('Class Name', validators=[DataRequired()])
    zoom_link = StringField('Zoom Link', validators=[DataRequired()])
    submit = SubmitField('Add Session')

class AddReviewForm(FlaskForm):
    tutor = IntegerField('Tutor', validators=[DataRequired()])
    session = IntegerField('Session', validators=[DataRequired()])
    subject = StringField('Subject', validators=[DataRequired()])
    class_num = IntegerField('Class Number', validators=[DataRequired()])
    comment = StringField('Comment', validators=[DataRequired()])
    rating_num = FloatField('Rating', validators=[DataRequired()])
    submit = SubmitField('Add Review')