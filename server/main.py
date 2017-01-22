from flask import Flask, render_template, request, send_from_directory
from blueprint import spotify
from globals import IS_PRODUCTION

app = Flask(__name__, static_url_path="")

app.register_blueprint(spotify.sp_app)


@app.route("/")
def index():
    token = request.cookies.get("spotify_token")
    return render_template("index.html", has_spotify_token=token is not None)


if not IS_PRODUCTION:
    @app.route("/static/<path:path>")
    def serve_static(path):
        return send_from_directory("static_files", path)


if __name__ == "__main__":
    app.run()
