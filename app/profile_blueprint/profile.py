import re

from flask import Blueprint, render_template, flash, jsonify, request

from flask_login import login_required, current_user

from app.models import Selection

from app import db

profile_bp = Blueprint('profile_bp', __name__)

dateFormat = re.compile('[^%22][\d]+') # regular expression object to parse the data from the client

@profile_bp.route('/user/<username>/')
@login_required
def user_profile(username):

    return render_template('user_profile.html') # not sure how to handle the variables at this point

# need a route to call when saving selections
@profile_bp.route('/save/', methods=['POST'])
@login_required
def save():
    # we can learn alittle regex to parse the data input
    data = request.get_data()
    selections = dateFormat.findall(str(data))
    # have the date strings here. make the new Selection entries into the db
    for date in selections:
        new_sel = Selection(date_string=date, user=current_user)
        db.session.add(new_sel)
        print("Date added to db:", date)
    db.session.commit()

    return jsonify("Test Save")


"""
Possible Future Routes:

Profile Page

Settings

Feedback



"""

