from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "Hello, this is PetFax"
    
    from . import pets
    app.register_blueprint(pets.bp)

    return app