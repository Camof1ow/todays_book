from flask import Flask, render_template, request, jsonify, redirect
from pymongo import MongoClient
import jwt
import datetime
import hashlib
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
import os

client = MongoClient(os.environ.get("MONGO_DB_PATH"))

SECRET_KEY = 'password'

db = client.dbsparta

app = Flask(__name__)

if __name__ == '__main__':

    app.run('0.0.0.0', port=8000, debug=True)

