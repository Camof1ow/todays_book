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

@blueprint.route("/comment", methods=["POST"])
def bucket_done():
    star_receive = request.form['star_give']
    comment_receive = request.form['comment_give']
    id_receive = request.form['id_give']
    date_receive = request.form['date_give']

    db.bookcomment.insert_one({'star':star_receive,'comment':comment_receive,'id':id_receive , 'date':date_receive  })
    return jsonify({'msg': '댓글등록완료!'})

@blueprint.route("/comment", methods=["GET"])
def comment_get():
    book_comment = list(db.bookcomment.find({}, {'_id': False}))
    print(book_comment)
    return jsonify({'book_comment': book_comment})


