from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__) # Flask class'ina aid olan bir instance yaradiriq burda ve adini da app qoyuruq.
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASEA_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)

from CLEANBLOG import routes