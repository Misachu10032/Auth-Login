from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, ValidationError
from db_utils import if_username_exist


class SignUpForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(
        "Username Error"), Length(min=6, max=20, message="Username Length Error"),])
    password = StringField('password', validators=[DataRequired(
        "Password Error"), Length(min=6, max=20, message="Password Length Error")])
    firstname = StringField('firstname', validators=[
                            DataRequired(message="Firstname Error")])
    lastname = StringField('lastname', validators=[
                           DataRequired(message="Lastname Error")])
    email = StringField('email', validators=[
                        DataRequired(message="Email Error")])

    def validate_username(self, username):

        existing_user = if_username_exist(username)

        if existing_user:
            raise ValidationError('That username is taken.')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
