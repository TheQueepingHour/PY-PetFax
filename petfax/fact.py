from flask import ( Blueprint, render_template) 
import json

bp = Blueprint('fact', __name__, url_prefix="/facts")

pets = json.load(open('pets.json'))

@bp.route('/')
def index(): 
    return render_template('facts/index.html', pets=pets)

@bp.route('/new')
def new(): 
    return render_template('facts/new.html')