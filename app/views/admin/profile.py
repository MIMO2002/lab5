from flask import Blueprint

profile_bp = Blueprint('profile_bp', __name__)

@profile_bp.route('/profile')
def profile():
    return 'This is profile, Admin/Profile'