from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return "Plinghee"


@app.route("/name")
def name():
    return "Shrijan"

if __name__ == "__main__":
    app.run()
