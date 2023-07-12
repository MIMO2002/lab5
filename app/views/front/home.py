from flask import Blueprint

home_bp = Blueprint('home_bp',__name__)

@home_bp.route('/home3')
def home3():
    return 'this is home3'