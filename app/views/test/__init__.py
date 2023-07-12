from flask import Blueprint, render_template
from .form import form_bp

test_bp = Blueprint('test_bp', __name__, url_prefix='/test')
test_bp.register_blueprint(form_bp)

@test_bp.route('/')
def test_home():
    return 'This is Test'