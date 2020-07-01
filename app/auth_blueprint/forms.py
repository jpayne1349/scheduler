
from flask_wtf import FlaskForm                             # base class, of which our classes will inherit from

from wtforms import StringField, SubmitField, PasswordField, BooleanField     # types of input

from wtforms.validators import InputRequired, ValidationError, Email, EqualTo

from app.models import User


# this will hold all of our form classes.

# we call this in each blueprint we'd like to use the form in.



class LoginForm(FlaskForm):
    # things needed to login are username, password
    # username could also be email...

    username = StringField('Username', [InputRequired()])

    password = PasswordField('Password', [InputRequired()])

    remember_me = BooleanField('Remember Me')

    submit = SubmitField('Sign In')



class RegistrationForm(FlaskForm):

    username = StringField('Username', validators=[InputRequired()])

    email = StringField('Email', validators=[InputRequired(), Email()])

    password = PasswordField('Password', validators=[InputRequired()])

    password2 = PasswordField(
        'Repeat Password', validators=[InputRequired(), EqualTo('password')])

    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')