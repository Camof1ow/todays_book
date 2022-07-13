import random
import jwt
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
    num = random.randrange(1, 40)
    Tbook = db.bookinfo.find_one({'rank': str(num)}, {'_id': False})
    print(Tbook['title'])
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        print(payload)
        return render_template('main.html', book=Tbook)
    except jwt.ExpiredSignatureError:
        return redirect('/')
    except jwt.exceptions.DecodeError:
        return redirect("/")



