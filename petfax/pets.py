from flask import (Blueprint, render_template)
import json

bp = Blueprint(
    'pets',
    __name__, 
    url_prefix="/pets"
    )

@bp.route("/")
def pets():
    pets = json.load(open("pets.json"))
    print(pets)
    return render_template(
        'index.html',
        title="This is PetFax",
        pets=pets,
        
    )
        
@bp.route("adopt")
def adopt():
    return "I have adopted a pet"
