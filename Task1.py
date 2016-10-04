from flask import Flask, render_template

from wtforms import Form, StringField, validators

class DemoForm(Form):
    test_name = StringField("Test", [validators.Length(min=4, max=128, message= 'No correct name')])
    test_email = StringField('Email',[validators.Email (message='No correct E-mail')] )
    test_comment = StringField ('Comment')


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    name = DemoForm()
    email = DemoForm()
    comment = DemoForm()
    return render_template("index.html", name=name, email=email, comment=comment)




if __name__ == '__main__':
    app.run(port=8888, debug=True)
