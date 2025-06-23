from flask import Flask
from .config import Config, db
from .models.comedian import Comedian
from .models.guest import Guest
from .models.appearance import Appearance

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from .controllers.routes import api
    app.register_blueprint(api)

    return app
