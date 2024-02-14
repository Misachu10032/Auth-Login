from flask import Flask
from flask_login import LoginManager
from flask_cors import CORS

app = Flask(__name__)
app.config.from_pyfile('config.py')
login_manager = LoginManager(app)
CORS(app)

from app import routes
