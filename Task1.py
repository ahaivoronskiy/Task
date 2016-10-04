from flask import Flask, render_template, request

from wtforms import Form, StringField, validators

class DemoForm(Form):
    test_name = StringField("Test", [validators.Length(min=4, max=128, message= 'No correct name')])
    test_email = StringField('Email',[validators.Email (message='No correct E-mail')] )
    test_comment = StringField ("Comment", [validators.Length(min=4,  message= 'Enter your comment')])
    test_phone = StringField ('Phone number')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = DemoForm(request.form)

    if request.method == 'POST' and form.validate():
        return "All data in form is valid"

    return render_template("index.html", form=form )

if __name__ == '__main__':
    app.run(port=8888, debug=True)