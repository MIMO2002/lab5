from flask import Blueprint

form_bp = Blueprint('form_bp', __name__)

@form_bp.route('/form')
def profile():
    return 'This is profile, Test/Form'