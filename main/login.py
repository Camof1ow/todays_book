from flask import Blueprint

blue_login = Blueprint("login", __name__,url_prefix="/login")

@blue_login.route("/read")
def read():
    return "this is read"

@blue_login.route("/write")
def write():
    return "this is write"
