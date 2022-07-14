from pages import *
from flask import Blueprint, Flask, render_template, request, jsonify, redirect
import requests
from pymongo import MongoClient

import hashlib
import os
import jwt
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.environ.get("CLIENT"))
SECRET_KEY = os.environ.get("PRIVATE_KEY")

db = client.dbsparta

blueprint = Blueprint("ranking", __name__, url_prefix='/ranking')


@blueprint.route("/")
def ranking():
    token_receive = request.cookies.get('mytoken')
    ranking_list = list(db.bookinfo.find({}, {'_id': False}))
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        print(payload)
        return render_template('ranking.html', rows=ranking_list)

    except jwt.ExpiredSignatureError:
        return "<script>alert(\'로그인 시간이 만료되었습니다.\');document.location.href=\"/login/?#\"</script>"
    except jwt.exceptions.DecodeError:
        return "<script>alert(\'로그인이 필요합니다.\');document.location.href=\"/login/?#\"</script>"


@blueprint.route('/rank', methods=['GET'])
def ranklist():
    ranking_list = list(db.bookinfo.find({}, {'_id': False}))
    return jsonify({'books': ranking_list})
