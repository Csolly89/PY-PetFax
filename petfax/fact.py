from flask import ( Blueprint, render_template, request, redirect )
from . import models 

bp = Blueprint('fact', __name__, url_prefix="/facts")

@bp.route('/')
def index(): 
    return render_template('facts/index.html')

@bp.route('/new', methods=["GET", "POST"])
def new():
    if request.method == "GET":
        return render_template("facts/new.html")
    else:
        submitter = request.form['submitter']
        fact = request.form['fact']
        new_fact = models.Fact(submitter=submitter, fact=fact)
        print(new_fact)
        models.db.session.add(new_fact)

        models.db.session.commit()
        print(request.form)
        return redirect('/facts')
        