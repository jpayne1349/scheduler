# pylint: disable=no-member, undefined-variable
 
from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash

from . import db

from flask_login import UserMixin

from . import login_manager



@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):                                     # the class is the table, calling this one User, inherits from Model class ** added in the UserMixin from flask-login
    id = db.Column(db.Integer, primary_key=True)                    # id is the primary key, specific to each "user/row", assigned by the database module
    username = db.Column(db.String(64), index=True, unique=True)    # each piece of info is a new Column, each unique "user" will be a row
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    posts = db.relationship('Post', backref='author', lazy='dynamic')   # added after creating the Post class.
                                                                        # defines 'Post' as the many side of this one-to-many relationship
                                                                        # a backwards reference adds the .author field to "post", adding in "post.author" functionality
                                                                        #
    selections = db.relationship('Selections', backref='user', lazy='dynamic')                                                                    

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)           # making user objects hash their passwords as they come into the system.

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)        # the hash check is done per user

    def __repr__(self):
        return '<User {}>'.format(self.username)                    # defines how the object will be printed when called from the interpreter
                                                                      # will be useful for debugging, other Users may be admin, dev, etc.

# we now need a selections table in order to store the dates selected by the user
# this will be changed when the database type changes. sqlite does not support arrays.
# none of these would be required. I don't know that if we submitted again on top, that it
# would update the row and not just create a new one.


class Selections(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    month = db.Column(db.Integer)
    week = db.Column(db.Integer)
    day_one = db.Column(db.Integer)
    day_two = db.Column(db.Integer)
    day_three = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Selection: Month: {month} Week: {week} Days: {day_one} {day_two} {day_three}>'

    # due to db.relationship above, class has selections.user attribute now



class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow) # passing in the function "datetime.utcnow" with no (), the timestamp will run this function at post creation
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))               # "user" is lowercase because it's referencing the name of the table according to SQLAlchemy, not our class name

    def __repr__(self):
        return '<Post {}>'.format(self.body)







