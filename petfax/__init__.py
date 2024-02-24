from flask import Flask
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:batman89@localhost:5432/petfax"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    @app.route("/")
    def index():
        return "Hello, this is PetFax"
    
    from . import pets
    app.register_blueprint(pets.bp)

    return app