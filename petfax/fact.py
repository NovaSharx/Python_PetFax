from flask import Blueprint, render_template
import json

bp = Blueprint('fact', __name__, url_prefix='/facts')

@bp.route('/new')
def new_fact():
    return render_template('new_fact.html')
