from flask import Flask

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db=SQLAlchemy()
migrate=Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models
    
    from .views import main_list, main_views
    app.register_blueprint(main_list.bp)
    app.register_blueprint(main_views.bp)

    return app

#if __name__ == "__main__":
#    app.run(host="localhost", port=config.PORT, debug=config.DEBUG_MODE)
