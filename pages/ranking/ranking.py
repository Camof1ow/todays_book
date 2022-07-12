from pages import *
from flask import Blueprint,Flask, render_template, request, jsonify, redirect
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

import hashlib
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.environ.get("mongodb+srv://test:sparta@cluster0.7nr2yln.mongodb.net/?retryWrites=true&w=majority") #pymongo db 경로
SECRET_KEY = os.environ.get("SPARTA")
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://series.naver.com/ebook/top100List.series',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

blueprint = Blueprint("ranking", __name__, url_prefix='/ranking')


@blueprint.route("/")
def ranking():
    return render_template('ranking.html')


#content > div > ul:nth-child(1) > li:nth-child(2) > a > span.writer writer
#content > div > ul:nth-child(1) > li:nth-child(2) > em star
#content > div > ul:nth-child(1) > li:nth-child(2) > a > strong title
#content > div > ul:nth-child(1) > li:nth-child(2) > a
#content > div > ul:nth-child(1) > li:nth-child(1) > a > strong
#content > div > ul:nth-child(1) > li:nth-child(1) > a

for page in range(1,6):

    raw = requests.get('https://series.naver.com/ebook/top100List.series?page=' + str(page))
    html = BeautifulSoup(raw.text, 'html.parser')

    book = html.select("div#content li")

    for books in book :
        rank = books.select_one("span.num").text
        title = books.select_one("a strong").text
        writer = books.select_one("span.writer").text
        score = books.select_one("em.score_num").text
        image = books.select_one('img')['src']

        doc = {
            'rank':rank,
            'title':title,
            'writer':writer,
            'score':score,
            'image':image
        }

@blueprint.route('/rank', methods=['GET'])
def show():
    ranking_list =list(db.bookinfo.find({},{'_id':False}))
    return jsonify({'books':ranking_list})

