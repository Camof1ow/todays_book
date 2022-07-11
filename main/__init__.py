from flask import Flask
from . import comment
from . import data
from . import login
from . import signup

app = Flask(__name__)

app.register_blueprint(comment.blue_comment)
app.register_blueprint(data.blue_data)
app.register_blueprint(login.blue_login)
app.register_blueprint(signup.blue_signup)

