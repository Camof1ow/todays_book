from flask import Blueprint

blue_signup = Blueprint("signup", __name__,url_prefix="/signup")

@blue_signup.route("/read")
def read():
    return "this is read"

@blue_signup.route("/write")
def write():
    return "this is write"
