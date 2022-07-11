from pages import *
from flask import Blueprint

blueprint = Blueprint("detail", __name__, url_prefix='/detail')


@blueprint.route("/")
def detail():
    return render_template('detail.html')
