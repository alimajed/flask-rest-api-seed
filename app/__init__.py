from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from marshmallow import ValidationError

from app.database.db import metadata
from config import ConfigFactory


db = SQLAlchemy(metadata=metadata)
migrate = Migrate()
marshmallow = Marshmallow()


def create_app():
    app = Flask(__name__)
    app.config.from_object(ConfigFactory.factory().__class__)

    # init extensions
    db.init_app(app)
    migrate.init_app(app, db)
    marshmallow.init_app(app)

    with app.app_context():
        # import blueprints
        from app.routes.home import home_bp
        from app.routes.user import user_bp

        # register blueprints
        app.register_blueprint(home_bp, url_prefix="/api/home")
        app.register_blueprint(user_bp, url_prefix="/api/user")

        # global handlers
        @app.errorhandler(ValidationError)
        def handle_marshmallow_validation(err):
            return jsonify(err.messages), 400

        return app