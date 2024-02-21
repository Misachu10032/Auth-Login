from flask import Flask, jsonify
from flask_login import LoginManager
##I was going to use LoginManager to store user session etc,but ran into some issue so I decided not to do it
from flask_cors import CORS


app = Flask(__name__)
app.config['SECRET_KEY'] = 'sercret key'
cors = CORS(app, resources={r"/api/*": {"origins": "*"}},credentials=True)
app.config['CORS_HEADERS'] = 'Content-Type'


from app import routes