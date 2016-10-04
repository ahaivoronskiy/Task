from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Task1 import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement= True )
    name = db.Column(db.String(128), unique=True)
    email = db.Column(db.String(256), unique=True)
    comment = db.Column (db.String, unique=True)
    phone = db.Column(db.String(128), unique=True)

    def __init__(self, name, email, comment, phone):
        self.email = email
        self.name = name
        self.comment = comment
        self.phone = phone

    def __repr__(self):
        return '<User %r>' % self.username
db.create_all()
