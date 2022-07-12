from pages import *
from flask import Blueprint

blueprint = Blueprint("detail", __name__, url_prefix='/detail')

from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient(os.environ.get("CLIENT")) #pymongo db 경로
SECRET_KEY = os.environ.get("PRIVATE_KEY") # Secret key
db = client.dbsparta

# import requests
# from bs4 import BeautifulSoup
#
# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)
#
# soup = BeautifulSoup(data.text, 'html.parser')

@blueprint.route("/")
def detail():
    return render_template('detail.html')
#
# @app.route("/book", methods=["POST"])
# def bucket_post():
#     sample_receive = request.form['sample_give']
#     print(sample_receive)
#     return jsonify({'msg': 'POST(기록) 연결 완료!'})

@blueprint.route("/detail", methods=["GET"])
def detail_get():
    book_list = list(db.bookinfo.find({}, {'_id': False}))
    print(book_list)
    return jsonify({'book': book_list})

