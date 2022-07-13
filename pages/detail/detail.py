from pages import *
from flask import Blueprint

blueprint = Blueprint("detail", __name__, url_prefix='/detail')

from pymongo import MongoClient
import certifi
import jwt

ca = certifi.where()

client = MongoClient(os.environ.get("CLIENT"), tlsCAFile=ca)  # pymongo db 경로
SECRET_KEY = os.environ.get("PRIVATE_KEY")  # Secret key
db = client.dbsparta


@blueprint.route("/")
def detail():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        print(payload)
        return render_template('detail.html')
    except jwt.ExpiredSignatureError:
        return "<script>alert(\'로그인 시간이 만료되었습니다.\');document.location.href=\"login\"</script>"
    except jwt.exceptions.DecodeError:
        return "<script>alert(\'로그인이 필요합니다.\');document.location.href=\"login\"</script>"



@blueprint.route("/detail", methods=["GET"])
def detail_get():
    book_list = list(db.bookinfo.find({}, {'_id': False}))
    return jsonify({'book': book_list})
