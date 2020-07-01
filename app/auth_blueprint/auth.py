 

from flask import Blueprint, render_template, flash, redirect, url_for, request

#from flask import current_app as app

from .forms import LoginForm, RegistrationForm

from flask_login import current_user, login_user, logout_user

from app.models import User

from werkzeug.urls import url_parse

from app import db



authorization_bp = Blueprint('authorization_bp', __name__)


@authorization_bp.route('/register/', methods=['GET', 'POST'])
def register():

    if current_user.is_authenticated:
        return redirect(url_for('profile_bp.user_profile', username=current_user.username))

    form = RegistrationForm()

    if form.validate_on_submit():

        user = User(username=form.username.data, email=form.email.data)

        user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()

        flash('Congratulations, you are now a registered user!')

        return redirect(url_for('authorization_bp.login_page'))

    return render_template('register.html', form=form)


@authorization_bp.route('/login/', methods=['GET', 'POST'] )
def login_page():

    if current_user.is_authenticated:
        return redirect(url_for('public_access_bp.homepage'))

    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(username=form.username.data).first() # filtering the form info for the username portion, and stopping at the first that matches?

        if user is None or not user.check_password(form.password.data): # this is doing two checks. if the user was None, flash. and if the password was wrong, flash.
            flash('Invalid username or password')
            return redirect(url_for('authorization_bp.login_page'))

        login_user(user, remember=form.remember_me.data)                # if it makes it past that if statement, everything has checked out.

        next_page = request.args.get('next')

        if not next_page or url_parse(next_page).netloc != '':

            next_page = url_for('profile_bp.user_profile', username=current_user.username)

        return redirect(next_page)

    return render_template('login.html', form=form)


@authorization_bp.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('public_access_bp.homepage'))



"""
Possible Future Routes:

Reset Credentials

Sign Up / Create an Account



"""
