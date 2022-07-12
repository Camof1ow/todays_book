from pages import *
from flask import Blueprint

blueprint = Blueprint("login", __name__, url_prefix='/login')


@blueprint.route("/")
def login():
    return render_template('login.html')


# 로그인 API
@app.route('/api/login', methods=['POST'])
def api_login():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    nickname_receive = request.form['nickname_give']
    # pw 암호화.
    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()
    # id, pw, 닉네임으로 유저 찾기
    result = db.users.find_one({'id': id_receive, 'pw': pw_hash, 'nic': nickname_receive})
    # 찾은 후 토근 발급
    if result is not None:
        # 1시간 후 자동 종료
        payload = {
            'id': id_receive,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256').decode('utf-8')
        # token을 줍니다.
        return jsonify({'result': 'success', 'token': token})
    # 찾지 못하면
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})

