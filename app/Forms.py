from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class RegisterForm(Form):
	username = StringField('username', validators=[DataRequired()])
	password = PasswordField('password', validators=[DataRequired()])
    #remember_me = BooleanField('remember_me', default=False)
    # e-mail
    #?!social network profile