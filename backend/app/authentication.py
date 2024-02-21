from flask_login import UserMixin
from .db_utils import get_user_by_username

def validate_password_and_get_user(username, password):
    user_data = get_user_by_username(username)
    if user_data is not None and user_data.get('password') == password :
        return user_data
    else:
        return None



# add hash later for security
