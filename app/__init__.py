"""
General Comments/Thoughts with TODO:

5/31/20 -
    TODO: Incorporate the "last seen" capability for future group use? maybe
    We have users. We have a way of registering them, signin/signout, etc.
    The user profile page needs work. And figuring out how to set that up will be a challenge.
    IDEA: have two different calendars, a personal selection calendar. Like your personal schedule, you could screenshot.
        and then the common calendar, where everyone's selections are merged. before/after the algorthim
    Still need to figure out how the algorithm will run, and how the user will submit their selections.
    The calendar peices will need identifiers that correspond with the actual date.
    Selecting the days may require javascript, or something like that. Unsure.
    Moving toward a functional calendar would be a good next step. And not worry so much about the aesthetics of the site, for now.
        Each day would be an individual selection, and days that are concurrent would be joined in "style"
        The date of each selection would have to stored in the database, possibly as a list or dictionary.
        A list would work if no preferences are given. Which would require altering the algorithm.
    Say you had a list of three dates such as ([month day year, month day year, month day year])
    With each list being it's own seperate week. i.e. the seven day period for each three day selection.
    So each person would need that list within a list. similar to the algorithms way of organizing preference lists
    The dates will be the hardest. Some convention must be used in order decipher.
    It worked well when you treated the week as a list of 0 through 6. You would then have to convert that each month.
    SOmEhoW. To be robust. You would want the application to determine what date the start of the week was.
    Or if you were using the actual dates, it would just need to know that only three per week could be selected.
    WE can start out with just making selections on the calendar...
    Pretty sure I will have to write my own Javascript to select items on the calendar. Let's learn that.




"""



from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()

login_manager = LoginManager()

def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)

    app.config.from_object('config.DevelopmentConfig') # grabbing the development config class out of config.py
    # our config file will be located elsewhere

    db.init_app(app)
    migrate.init_app(app, db)

    login_manager.init_app(app)

    login_manager.login_view = 'authorization_bp.login_page'

    # this is voodoo magic...
    # all 'pieces' of the app must be brought in inside this context function
    # this is supplying the already created app with the resources inside the app folder
    with app.app_context():

        from .public_access_blueprint import public_access # giving the app access to this folder and this file
        from .profile_blueprint import profile
        from .auth_blueprint import auth
        from .errors_blueprint import error_handlers


        app.register_blueprint(public_access.public_access_bp)  # registering the blueprint inside that file
        app.register_blueprint(profile.profile_bp)
        app.register_blueprint(auth.authorization_bp)
        app.register_blueprint(error_handlers.error_handlers_bp)

        from . import models  # the period means this directory, import those two modules


        return app


