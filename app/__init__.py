from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app.database.db import metadata
from config import ConfigFactory


db = SQLAlchemy(metadata=metadata)
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(ConfigFactory.factory().__class__)

    # init extensions
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        # import blueprints
        from app.routes.home import home_bp

        # register blueprints
        app.register_blueprint(home_bp, url_prefix="/api/home")

        return app