from flask import Flask
from flask_migrate import Migrate
from server.models.models import db
from server.controllers.routes import api
from flask_jwt_extended import JWTManager
import os

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'postgresql://erykah:ika123@localhost:5432/late_show_db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'super-secret')

    db.init_app(app)
    migrate = Migrate(app, db)
    jwt = JWTManager(app)

    app.register_blueprint(api)

    return app