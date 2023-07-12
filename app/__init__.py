from flask import Flask
from flask_wtf.csrf import CSRFProtect
from app.config import Config

def create_app():
    app = Flask(__name__)
    
    # Load flask configuration
    config = Config()
    app.config.from_object(config)
    
    # Register blueprint
    from .views import register_blueprint
    register_blueprint(app)
    
    return app