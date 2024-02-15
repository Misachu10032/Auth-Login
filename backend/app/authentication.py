from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, user_id, username, password):
        self.id = user_id
        self.username = username
        self.password = password

    @staticmethod
    def check_password(saved_password, provided_password):
        return saved_password == provided_password
    

#add hash later for security