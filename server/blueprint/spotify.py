from flask import Blueprint, redirect, make_response, request
from globals import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URL
from spotipy.oauth2 import SpotifyOAuth
from api.spotify import current_user_context
from integration.spotify import createPlaylist

sp_app = Blueprint("sp_app", __name__)

AUTH = SpotifyOAuth(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URL, scope="playlist-modify-public")


@sp_app.route("/spotify/login")
def login_redirect():
    return redirect(AUTH.get_authorize_url())


@sp_app.route("/spotify/callback")
def callback():
    resp = make_response(redirect("/"))
    code = request.args.get("code")
    spotify_token = AUTH.get_access_token(code)["access_token"]
    resp.set_cookie("spotify_token", spotify_token)
    return resp


@sp_app.route("/api/spotify/playlist", methods=["POST"])
def create_playlist():
    token = request.cookies.get("spotify_token")
    user_id = current_user_context(token)["id"]
    body = request.get_json()
    subreddit = body["subreddit"]
    playlist_name = body["playlist_name"]

    createPlaylist(token, user_id, subreddit, playlist_name)
    return ""
