from flask import Flask, render_template, request, redirect, session
from wtforms import Form, StringField, validators, PasswordField
from flask_sqlalchemy import SQLAlchemy
import datetime, config



class DemoForm(Form):
    test_name = StringField("Name", [validators.Length(min=4, max=128, message= 'No correct name')])
    test_email = StringField('Email',[validators.Email (message='No correct E-mail')] )
    test_comment = StringField ("Comment", [validators.Length(min=4,  message= 'Enter your comment')])
    test_phone = StringField ('Phone number')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
app.config.from_object('config')

class Guestbook(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement= True )
    name = db.Column(db.String(128))
    email = db.Column(db.String(256))
    comment = db.Column (db.Text)
    phone = db.Column(db.String(128))
    date = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, name, email, comment, phone):
        self.email = email
        self.name = name
        self.comment = comment
        self.phone = phone

db.create_all()

class Login(Form):
    log = StringField ('log')
    password = PasswordField ('password')
@app.route('/login.html', methods= ['GET', 'POST'])
def login():
    form = Login(request.form)
    if request.method == 'POST' and form.validate():
        if config.log == form.log.data and config.password == form.password.data:
            form.log == True
            return redirect(url_for('index'))
    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def index():

    form = DemoForm(request.form)

    if request.method == 'POST' and form.validate():
        record = Guestbook(
            email=form.test_email.data,
            name=form.test_name.data,
            comment=form.test_comment.data,
            phone=form.test_phone.data
        )
        db.session.add(record)
        db.session.commit()

        return redirect(request.referrer)


    return render_template("index.html", form=form, log=session.get('log'), record=Guestbook.query.all()  )

@app.route('/delete/<int:record_id>', methods={'GET', 'POST'})
def delete(record_id=None):
    record = Guestbook.query.get(record_id)
    db.session.delete(record)
    db.session.commit()

    return redirect(request.referrer)

if __name__ == '__main__':
    app.run(port=8888, debug=True)
