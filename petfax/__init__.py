#config
from flask import Flask
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return 'Hello, PetFax! <a href="/pets">Click here for pet index</a>'
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:PostGRE0420@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)
    
    from . import (pet, fact)
    app.register_blueprint(pet.bp)
    app.register_blueprint(fact.bp)

    return app