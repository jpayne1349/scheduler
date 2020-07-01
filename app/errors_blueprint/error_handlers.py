
from flask import Blueprint, render_template

#from flask import current_app as app




error_handlers_bp = Blueprint('error_handlers_bp', __name__)



@error_handlers_bp.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
                           
                           
                           
"""
Possible Future Routes:

ALL OTHER ERROR CODES?

Confirm Form Resubmission Problem

403

500 - Internal Server Error

etc.


"""