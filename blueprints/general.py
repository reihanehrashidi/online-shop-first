from flask import Blueprint

app = Blueprint("general", __name__)

@app.route("/")
def hello():
    return "this is main page"