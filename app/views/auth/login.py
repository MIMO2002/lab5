from flask import Blueprint, render_template, request
from .form import LoginForm


login_bp = Blueprint('login_bp', __name__)

@login_bp.route('/login', methods = ['GET','POST'])
def login():
    login_form = LoginForm()
    if request.method == 'GET':
        login_form.txt_username = "My Username"
        login_form.txt_password = "MyPass"
    else:
        username = login_form.txt_username.data
        password = login_form.txt_password.data
    data = {
        'title':'Login'
    }
    return render_template('auth/login.html', data = data, login_form = login_form)

@login_bp.route('/recovery')
def recovery():
    return 'Reocvery your password'

@login_bp.route('/register')
def register():
    return 'Register yourself'