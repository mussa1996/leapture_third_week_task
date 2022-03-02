# from flask_wtf import FlaskForm
# from wtforms import SubmitField, StringField, validators
# class EduCBASignUp(FlaskForm):
#  nameField = StringField('Name', [validators.Length(min=1)])
#  emailField = StringField('E-mail', [validators.Length(min=6, max=35)])
#  newsletterField = SubmitField('Sign me up')

from os import urandom
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
 
app = Flask(__name__, template_folder='.')
app.config['SECRET_KEY'] = urandom(16)
 
 
# user form class
class WelcomeUserForm(FlaskForm):
    name = StringField(label='Enter name: ',
                       validators=[
                           DataRequired(message='Name is required'),
                           Length(min=4, message='Name must be greater than %(min)d characters')
                       ])
    submit = SubmitField(label='Submit')
@app.route('/', methods=['GET', 'POST'])
def welcome():
    form = WelcomeUserForm()
    if form.validate_on_submit():
        return f'''<h4>Hello {form.name.data}</h4>'''
 
    return render_template('form.html',form=form)
 
# driver code
if __name__ == '__main__':
    app.run(debug=False)