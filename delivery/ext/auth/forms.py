from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField


class UserForm(FlaskForm):
    email = StringField("Email", [validators.DataRequired(), validators.Email()])
    password = PasswordField("Senha", [validators.DataRequired()])
    
    

