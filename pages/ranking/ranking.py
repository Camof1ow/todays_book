from pages import *
from flask import Blueprint, Flask, render_template, request, jsonify, redirect
import requests
from pymongo import MongoClient

import hashlib
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.environ.get("CLIENT"))
SECRET_KEY = os.environ.get("PRIVATE_KEY")

db = client.dbsparta

blueprint = Blueprint("ranking", __name__, url_prefix='/ranking')


@blueprint.route("/")
def ranking():
    return render_template('ranking.html')

@blueprint.route('/rank', methods=['GET'])
def ranklist():
    ranking_list =list(db.bookinfo.find({},{'_id':False}))
    return jsonify({'books':ranking_list})

