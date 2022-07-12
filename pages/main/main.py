from pages import *
from flask import Blueprint

blueprint = Blueprint("main", __name__, url_prefix='/')


@blueprint.route("/")
def home():
    return render_template('index.html')

@blueprint.route("/main")
def mainpage():
    return render_template('main.html')
