from flask import Flask, jsonify
from blueprint import spotify

app = Flask(__name__)

app.register_blueprint(spotify.sp_app)

if __name__ == "__main__":
    app.run()
