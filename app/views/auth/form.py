from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    txt_username = StringField("Username", validators=[DataRequired()])
    txt_password = StringField("Password", validators=[DataRequired()])
    chk_remember_me = BooleanField("Remember me")
    btn_login = SubmitField("Log In")