from wtforms import Form, StringField, PasswordField, validators
from wtforms.validators import DataRequired, Length, ValidationError
from .db_utils import if_username_exist

#Rest Input validation
class SignUpForm(Form):
    print('sdacca')
    username = StringField('Username', validators=[
                           validators.DataRequired(), validators.Length(min=4, max=25)])
    password = PasswordField('Password', validators=[
                             validators.DataRequired(), validators.Length(min=6)])
    firstname = StringField('First Name', validators=[
                            validators.DataRequired(), validators.Length(max=50)])
    lastname = StringField('Last Name', validators=[
                           validators.DataRequired(), validators.Length(max=50)])
    email = StringField('Email', validators=[
                        validators.DataRequired(), validators.Length(max=50)])

    def validate_username(form, field):
        print('here')
        username = field.data
        print(username,'usernmae')
        existing_user = if_username_exist(username)

        if existing_user:
            print('we heres')
            raise ValidationError('That username is taken.')


class LoginForm(Form):
    username = StringField('Username', validators=[
                           DataRequired(), Length(min=2, max=20)])
    password = StringField('Password', validators=[DataRequired()])


