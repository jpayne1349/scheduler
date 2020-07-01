 

from flask import Blueprint, render_template, flash

from flask_login import login_required

#from flask import current_app as app




profile_bp = Blueprint('profile_bp', __name__)


#month_day_count = 31


@profile_bp.route('/user/<username>/')
@login_required
def user_profile(username):


    return render_template('user_profile.html') # not sure how to handle the variables at this point


"""
Possible Future Routes:

Profile Page

Settings

Feedback



"""

