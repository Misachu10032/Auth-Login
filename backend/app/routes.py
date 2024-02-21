from flask import request, jsonify
from app import app
from .db_utils import create_user,get_all_users_from_db,get_all_products_from_db,get_user_by_id_from_db,delete_user_by_id_from_db
from .authentication import validate_password_and_get_user
from .forms import SignUpForm, LoginForm
from flask_cors import cross_origin

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
    print('we in login')

    
    form = LoginForm(request.form)
   
    if form.validate():
        user = validate_password_and_get_user(form.username.data,form.password.data)
        if  user is not None:
            print(user)
            return jsonify({'message': 'Login successful','user': user}), 200
        else:
            return jsonify({'error': 'incorrect username or password'}), 401
    else:
        return jsonify({'error': 'incorrect input form'}), 401


@app.route('/api/logout', methods=['POST'])
def logout():

    return jsonify({'message': 'Logout successful'}), 200


@app.route('/api/get_all_users', methods=['GET'])
def get_all_users():
    user_list=get_all_users_from_db()
    print(user_list)
    return jsonify({'message': 'Login successful','user_list':user_list}), 200


@app.route('/api/get_all_products', methods=['GET'])
def get_all_products():
    product_list=get_all_products_from_db()
    print(product_list)
    return jsonify({'message': 'Login successful','product_list':product_list}), 200

@app.route('/api/get_user_by_id/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):

    user=get_user_by_id_from_db(user_id)
    print(user,"routes")
    return jsonify({'message': 'Login successful','user': user}), 200


@app.route('/api/delete_user_by_id/<int:user_id>', methods=['DElETE'])
def delete_user_by_id(user_id):

    delete_user_by_id_from_db(user_id)
    return jsonify({'message': 'User Deleted'}), 200
