from pages import *
from flask import Blueprint

blueprint = Blueprint("detail", __name__, url_prefix='/detail')

from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient(os.environ.get("CLIENT"), tlsCAFile=ca) #pymongo db 경로
SECRET_KEY = os.environ.get("PRIVATE_KEY") # Secret key
db = client.dbsparta


@blueprint.route("/")
def detail():
    return render_template('detail.html')


@blueprint.route("/detail", methods=["GET"])
def detail_get():
    book_list = list(db.bookinfo.find({}, {'_id': False}))
    return jsonify({'book': book_list})

