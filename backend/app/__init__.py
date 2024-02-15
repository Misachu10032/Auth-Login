from flask import Flask, jsonify
from flask_cors import CORS

from .db_utils import test

app = Flask(__name__)

CORS(app)


@app.route('/api/abc', methods=['GET'])
def sdadsad():
    aa = 'aa'
    cc=test(aa)
    print(cc)

    return jsonify({'message': 'logged in'}), 200