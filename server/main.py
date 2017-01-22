from flask import Flask, render_template, request
from blueprint import spotify

app = Flask(__name__)

app.register_blueprint(spotify.sp_app)


@app.route("/")
def index():
    token = request.cookies.get("spotify_token")
    return render_template("index.html", has_spotify_token=token is not None)

if __name__ == "__main__":
    app.run()
