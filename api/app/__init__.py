from dotenv import load_dotenv
from flask import Flask

from app.config import Config
from app.extensions import db, migrate
from app.routes import register_blueprint


def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from app import models

    register_blueprint(app)

    return app
