from api.reddit import get_posts
from integration import get_filtered_posts
from api.spotify import findSong

import spotipy
import spotipy.util as util


def get_tracks(subreddit):
    """
    Return list of tracks.
    :type subreddit str
    :rtype list[dict]
    """

    posts = get_filtered_posts(subreddit)

    tracks = [
        findSong(post.title)
        for post
        in posts
    ]

    tracks = [
        track
        for track in tracks
        if track is not None
    ]

    return tracks


def createPlaylist(token, user, subreddit, playlist_name):
    sp = spotipy.Spotify(auth=token)
    playlist = sp.user_playlist_create(user, playlist_name)
    tracks = get_tracks(subreddit)
    tracks = [t["uri"] for t in tracks]
    sp.user_playlist_add_tracks(user, playlist['id'], tracks)

