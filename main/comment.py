from flask import Blueprint

blue_comment = Blueprint("comment", __name__,url_prefix="/comment")

@blue_comment.route("/read")
def read():
    return "this is read"

@blue_comment.route("/write")
def write():
    return "this is write"
