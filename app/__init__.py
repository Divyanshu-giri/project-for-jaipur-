from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'  # Change in production

    # Register blueprints here later
    from . import routes
    app.register_blueprint(routes.bp)

    return app
