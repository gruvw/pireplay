from flask import Flask


server = Flask(__name__)


@server.route("/")
def home():
    return "<p>Hello, World!</p>"
