from pages import *
from flask import Blueprint

blueprint = Blueprint("login", __name__, url_prefix='/login')


@blueprint.route("/")
def login():
    return render_template('login.html')



