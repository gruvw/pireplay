from flask import Flask


server = Flask(__name__)


@server.route("/")
def home():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    server.run(debug=True, host="0.0.0.0", port=80)
