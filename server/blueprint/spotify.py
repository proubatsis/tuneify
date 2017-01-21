from flask import Blueprint, redirect, make_response, request
from globals import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URL
from spotipy.oauth2 import SpotifyOAuth

sp_app = Blueprint("sp_app", __name__)

AUTH = SpotifyOAuth(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URL, scope="playlist-modify-public")

@sp_app.route("/spotify/login")
def login_redirect():
    return redirect(AUTH.get_authorize_url())


@sp_app.route("/spotify/callback")
def callback():
    resp = make_response()
    code = request.args.get("code")
    spotify_token = AUTH.get_access_token(code)["access_token"]
    resp.set_cookie("spotify_token", spotify_token)

    return resp
