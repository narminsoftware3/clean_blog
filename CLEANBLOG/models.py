from CLEANBLOG import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False) # nullable = False bu alanin bos ola bilmeyeceyini gosterir.
    email = db.Column(db.String, unique = True, nullable = False) # unique = True yeni email'lerin bir defe istifade olunmasini isteyirik.
    password = db.Column(db.String, nullable = False)
    posts = db.relationship('Post', backref = 'user', lazy = True)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return f'User: {self.name}, {self.email}'


class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, nullable = False)
    subtitle = db.Column(db.String, nullable = False)
    post_date = db.Column(db.DateTime, nullable = False, default = datetime.now().strftime('%Y-%m-%d'))
    post_text = db.Column(db.Text, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __init__(self, title, subtitle, post_text):
        self.title = title
        self.subtitle = subtitle
        self.post_text = post_text

    def __repr__(self):
        return f'Post: {self.title}, {self.subtitle}'

