from flask import Flask, render_template, request, redirect
from wtforms import Form, StringField, validators
from flask_sqlalchemy import SQLAlchemy

class DemoForm(Form):
    test_name = StringField("Test", [validators.Length(min=4, max=128, message= 'No correct name')])
    test_email = StringField('Email',[validators.Email (message='No correct E-mail')] )
    test_comment = StringField ("Comment", [validators.Length(min=4,  message= 'Enter your comment')])
    test_phone = StringField ('Phone number')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Guestbook(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement= True )
    name = db.Column(db.String(128))
    email = db.Column(db.String(256))
    comment = db.Column (db.Text)
    phone = db.Column(db.String(128))

    def __init__(self, name, email, comment, phone):
        self.email = email
        self.name = name
        self.comment = comment
        self.phone = phone

db.create_all()

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

    return render_template("index.html", form=form )



if __name__ == '__main__':
    app.run(port=8888, debug=True)







