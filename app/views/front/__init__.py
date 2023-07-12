from flask import Blueprint,render_template
from .home import home_bp

front_bp = Blueprint('front_bp',__name__)
front_bp.register_blueprint(home_bp)

@front_bp.route('/')
def home():
    return render_template('front/home.html')

@front_bp.route('/home2')
def home2():
    title="Home Page"
    return render_template('/front/home.html', title=title)