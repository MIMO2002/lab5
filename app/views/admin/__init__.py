from flask import Blueprint
from .profile import profile_bp

admin_bp = Blueprint('admin_bp', __name__, url_prefix='/admin')
admin_bp.register_blueprint(profile_bp)

@admin_bp.route('/')
def admin_home():
    return 'This is admin'