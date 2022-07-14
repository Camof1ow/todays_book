## __init__.py

from flask import Flask, render_template, request, jsonify, redirect
from pymongo import MongoClient
import datetime
import hashlib
import os
from dotenv import load_dotenv


load_dotenv() #환경변수 호출

client = MongoClient(os.environ.get("CLIENT")) #pymongo db 경로
SECRET_KEY = os.environ.get("PRIVATE_KEY") # Secret key
db = client.dbsparta
app = Flask(__name__) #app 객체선언
m = hashlib.sha256() #hash

from .main import main  # main.py 내용 호출
from .detail import detail
from .login import login

from .ranking import ranking


app.register_blueprint(main.blueprint) # main module
app.register_blueprint(login.blueprint) # login module
app.register_blueprint(detail.blueprint) # signup module

app.register_blueprint(ranking.blueprint) # ranking module

@app.before_request
def before_request():
    scheme = request.headers.get('X-Forwarded-Proto')
    if scheme and scheme == 'http' and request.url.startswith('http://'):
        url = request.url.replace('http://', 'https://', 1)
        code = 301
        return redirect(url, code=code)

if __name__ == '__main__':

    app.run('0.0.0.0', port=8000, debug=True)


