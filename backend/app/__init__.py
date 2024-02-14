from flask import Flask
from flask_login import LoginManager
from flask_cors import CORS
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config.from_pyfile('config.py')
mysql = MySQL(app)
login_manager = LoginManager(app)
CORS(app)


from app import routes
