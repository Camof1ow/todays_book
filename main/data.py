from flask import Blueprint

blue_data = Blueprint("data", __name__,url_prefix="/data")

@blue_data.route("/data")
def read():
    return "this is read"

@blue_data.route("/write")
def write():
    return "this is write"
