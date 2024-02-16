from flask import Flask, jsonify
from flask_login import LoginManager
from flask_cors import CORS
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sercret key'
CORS(app)



from app import routes