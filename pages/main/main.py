import random

from pages import *
from flask import Blueprint
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient(os.environ.get("CLIENT"))
db = client.dbsparta


blueprint = Blueprint("main", __name__, url_prefix='/')


@blueprint.route("/")
def home():
    return render_template('index.html')

@blueprint.route("/main")
def mainpage():
    return  render_template("main.html")

@blueprint.route("/Tbook", methods=["GET"])
def get_Tbook():
    num = random.randrange(1,40)
    Tbook = db.bookinfo.find_one({'rank':str(num)},{'_id':False})

    return jsonify({'Tbook':Tbook})




