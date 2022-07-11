from pages import *
from flask import Blueprint

blueprint = Blueprint("signup", __name__, url_prefix='/signup')


@blueprint.route("/")
def signup():
    return render_template('signup.html')
