from flask import Flask
from app.error_handlings import register_error_handlers  # Importing error handlers

def create_app():
    app = Flask(__name__)

    # Import and register routes
    from app import routes
    app.register_blueprint(routes.bp)

    # Register error handler
    register_error_handlers(app)

    return app
