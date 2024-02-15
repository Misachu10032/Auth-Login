from flask import request, jsonify
from flask_login import current_user, login_user, logout_user
from app import app
from .db_utils import create_user, get_user_by_username
from .authentication import User
from .forms import SignUpForm, LoginForm


@app.route('/api/sign_up', methods=['POST'])
def sign_up():

    form = SignUpForm(request.form)
    if form.validate_username(form.username.data):
        create_user(form.username.data,
                    form.password.data,
                    form.firstname.data,
                    form.lastname.data,
                    form.email.data,)
        return jsonify({'message': 'Signed up successfully'}), 201
    return jsonify({'message': form.errors}), 400


@app.route('/api/login', methods=['POST'])
def login():
    form = LoginForm(request.form)
    if form.validate():
        
        user_data = get_user_by_username(form.username)

        if user_data and User.check_password(user_data['password'], form.password.data):
            user = User(username=user_data['username'],
                        password=user_data['password'])
            login_user(user)
            return jsonify({'message': 'Login successful'}), 200
        else:
            return jsonify({'error': 'Invalid username or password'}), 401
    return jsonify({'error': form.errors}), 400


@app.route('/api/logout', methods=['POST'])
def logout():
    if current_user.is_authenticated:
        logout_user()
        return jsonify({'message': 'Logout successful'}), 200
    else:
        return jsonify({'error': 'You are not logged in'}), 401

@app.route('/api/current_user', methods=['GET'])
def current_user_exist():
  print("sdasd")
  if current_user.is_authenticated:
    return jsonify({'message':'loged in'}), 200
  return jsonify({'message':'log in required'}), 400


@app.route('/api/aaa', methods=['GET'])
def sdadsad():
  print("sdasd cjecl")
  user = User(username='username',
                password='password',user_id='username')
  login_user(user)
  return jsonify({'message':'loged in'}), 200
 