from flask import Flask
from flask_migrate import Migrate
from . import models
from . import pet
from . import fact

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:batman89@localhost:5432/petfax"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    @app.route("/")
    def index():
        return "Hello, this is PetFax"
    
    app.register_blueprint(pet.bp)
    app.register_blueprint(fact.bp)

    return app