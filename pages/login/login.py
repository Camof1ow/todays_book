from datetime import timedelta
import jwt
from pages import *
from flask import Blueprint, url_for

blueprint = Blueprint("login", __name__, url_prefix='/login')


@blueprint.route("/")
def login():
    return render_template('login.html', title='오늘의 책📚-로그인')


# 로그인 API
@app.route('/login', methods=['POST'])
def login():
    # 아이디 비밀번호 확인
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']
    pw_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    result = db.users.find_one({'username': username_receive, 'password': pw_hash})

    if result is not None:
        payload = {
            'id': username_receive,
            'exp': datetime.datetime.utcnow() + timedelta(seconds=10)  # 로그인 24시간 유지
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return jsonify({'result': 'success', 'token': token, 'msg': username_receive+' '+'님 환영합니다.'})
    # 찾지 못하면
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})


# [유저 정보 확인 API]
@app.route('/login/check', methods=['POST'])
def logincheck():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        print(payload)
        return jsonify({'result': 'success'})
    except jwt.ExpiredSignatureError:
        return redirect('/')
    except jwt.exceptions.DecodeError:
        return redirect('/')
