from flask import (Blueprint, render_template )
import json

pets = json.load(open('pets.json'))
# print(pets)

bp = Blueprint(
    'pet',
    __name__, 
    url_prefix="/pets"
)

@bp.route('/')
def index(): 
    return render_template(
        'pets/index.html', 
        title = "This Is PetFax",
        pets=pets)

# show route
@bp.route('/<int:id>')
def show(id): 
    pet = pets[id - 1]
    return render_template('pets/show.html', pet=pet)


# @bp.route("adopt", methods=["POST"])
# def adopt():
#     print(request.form)
#     return "I have adopted a pet"

# @bp.route('/<fact_id>', methods=["DELETE", "POST"])
# def delete(fact_id):
#     fact = models.Fact.query.get(fact_id)
#     if request.methods == "DELETE":
#         models.db.session.delete(fact)
#     else: 
#         fact.submitter = ""
#     models.db.session.commit()
#     return redirect("/facts")
