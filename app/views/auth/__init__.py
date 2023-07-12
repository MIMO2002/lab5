from flask import Blueprint
from .login import login_bp

auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth')
auth_bp.register_blueprint(login_bp)

@auth_bp.route('/')
def admin_home():
    return 'This is admin'