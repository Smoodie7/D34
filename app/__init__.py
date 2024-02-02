from flask import Flask
#from flask_limiter import Limiter
#from flask_limiter.util import get_remote_address
from app.error_handlings import register_error_handlers  # Importing error handlers

def create_app():
    app = Flask(__name__)
    #limiter = Limiter(app, key_func=get_remote_address, default_limits=["1000 per day", "100 per hour"])

    # Import and register routes
    from app import routes
    app.register_blueprint(routes.bp)

    # Register error handler
    register_error_handlers(app)

    return app
