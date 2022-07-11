from pages import *
from flask import Blueprint

blueprint = Blueprint("ranking", __name__, url_prefix='/ranking')


@blueprint.route("/")
def ranking():
    return render_template('ranking.html')
