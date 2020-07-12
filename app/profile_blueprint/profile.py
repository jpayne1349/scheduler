import re

from flask import Blueprint, render_template, flash, jsonify, request

from flask_login import login_required, current_user

from app.models import Selection, User

from app import db

profile_bp = Blueprint('profile_bp', __name__)

dateFormat = re.compile('[^%22][\d]+') # regular expression object to parse the data from the client

@profile_bp.route('/user/<username>/')
@login_required
def user_profile(username):
    old_selections = Selection.query.filter(Selection.user==current_user).all()
    # we want to send these old_selections through to the javascript to populate the calendar
    print(old_selections)

    sel_list = []
    for each in old_selections:
        sel_list.append(each.date_string)

    return render_template('user_profile.html', old_selections=sel_list)

# need a route to call when saving selections
@profile_bp.route('/save/', methods=['POST'])
@login_required
def save():
    old_selections = Selection.query.filter(Selection.user==current_user).all()

    data = request.get_data()
    new_selections = dateFormat.findall(str(data))
    # we could just delete all the prior selections and then add the new ones in...?
    for each in old_selections:
        print("deleting date:",each)
        db.session.delete(each)

    for date in new_selections:
        new_sel = Selection(date_string=date, user=current_user)
        db.session.add(new_sel)
        print("Date added:", date)
    db.session.commit()
    # "response" sent to javascript
    return jsonify(new_selections)


"""
Possible Future Routes:

Profile Page

Settings

Feedback



"""

