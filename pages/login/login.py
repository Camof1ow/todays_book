from datetime import timedelta
import jwt
from pages import *
from flask import Blueprint, url_for

blueprint = Blueprint("login/?#", __name__, url_prefix='/login')


@blueprint.route("/")
def login():
    return render_template('login.html', title='오늘의 책📚-로그인')


# 로그인 API
@app.route("/login1", methods=['POST'])
def login1():
    # 아이디 비밀번호 확인
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']
    pw_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    result = db.users.find_one({'username': username_receive, 'password': pw_hash})
    if result is not None:
        payload = {
            'id': username_receive,
            'exp': datetime.datetime.utcnow() + timedelta(seconds=60*60)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return jsonify({'result': 'success', 'token': token, 'msg': username_receive+' '+'님 환영합니다.'})
    # 찾지 못하면
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})


# 토큰 미발급시 메인,랭킹,디테일 페이지 접근 불가
# 다른 페이지 .py 파일에 추가해야함
# @app.route('/login/check', methods=['POST'])
# def logincheck():
#     token_receive = request.cookies.get('mytoken')
#     try:
#         payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
#         print(payload)
#         return jsonify({'result': 'success'})
#     except jwt.ExpiredSignatureError:
#         return "<script>alert(\'로그인 시간이 만료되었습니다.\');document.location.href=\"login\"</script>"
#     except jwt.exceptions.DecodeError:
#         return "<script>alert(\'로그인이 필요합니다.\');document.location.href=\"login\"</script>"


# 회원가입 API
# id, pw, nickname을 받아서, mongoDB에 저장합니다.
# 저장하기 전에, pw를 sha256 방법(=단방향 암호화. 풀어볼 수 없음)으로 암호화해서 저장합니다.
@app.route('/signup', methods=['POST'])
def signup():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    nickname_receive = request.form['nickname_give']
    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()
    db.users.insert_one({'id': id_receive, 'pw': pw_hash, 'nick': nickname_receive})
    return jsonify({'result': 'success'})


@app.route('/check_dup', methods=['POST'])
def check_dup():
    username_receive = request.form['username_give']
    exists = bool(db.users.find_one({"username": username_receive}))
    return jsonify({'result': 'success', 'exists': exists})


@app.route('/sign_up/save', methods=['POST'])
def sign_up1():
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']
    nickname_receive = request.form['nickname_give']
    password_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    doc = {
        "username": username_receive,  # 아이디
        "password": password_hash,  # 비밀번호
        "nickname": nickname_receive,  # 닉네임
    }
    db.users.insert_one(doc)
    return jsonify({'result': 'success'})
