


from flask import Blueprint, render_template, flash

from flask import current_app as app

public_access_bp = Blueprint('public_access_bp', __name__)    # by default this should look in static and templates globally
                                                                                    # public url prefix may not work, organizational


# i guess all the routes of public access will live in here

# possibly another page for feedback/contact with a form integrated

# maybe an about page as well, although, that can be covered in the homepage

@public_access_bp.route('/')
@public_access_bp.route('/home')
def homepage():
    #flash("this is a flash")
    return render_template('homepage.html')



"""
Possible Future Routes:

Contact Us / Feedback



"""

