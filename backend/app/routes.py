from flask import request, jsonify
from app import app
from .db_utils import create_user,get_all_users_from_db,get_all_products_from_db
from .authentication import User
from .forms import SignUpForm, LoginForm


@app.route('/api/sign_up', methods=['POST'])
def sign_up():

    form = SignUpForm(request.form)

    if form.validate():
        create_user(form.username.data,
                    form.password.data,
                    form.firstname.data,
                    form.lastname.data,
                    form.email.data,)



        return jsonify({'message': 'Form validated successfully'}), 200
    else:
        errors = form.errors
        return jsonify({'errors': errors}), 400



@app.route('/api/login', methods=['POST'])
def login():
    form = LoginForm(request.form)
    if form.validate():



        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'error': 'Invalid username or password'}), 401


@app.route('/api/logout', methods=['POST'])
def logout():

    return jsonify({'message': 'Logout successful'}), 200


@app.route('/api/get_all_users', methods=['GET'])
def get_all_users():
    user_list=get_all_users_from_db()
    print(user_list)
    return jsonify({'message': 'Login successful'}), 200


@app.route('/api/get_all_products', methods=['GET'])
def get_all_products():
    product_list=get_all_products_from_db()
    print(product_list)
    return jsonify({'message': 'Login successful'}), 200

