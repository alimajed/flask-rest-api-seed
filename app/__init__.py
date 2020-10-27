from flask import Flask

from config import ConfigFactory


def create_app():
    app = Flask(__name__)
    app.config.from_object(ConfigFactory.factory().__class__)

    with app.app_context():
        # import blueprints
        from app.routes.home import home_bp

        # register blueprints
        app.register_blueprint(home_bp, url_prefix="/api/home")

        return app