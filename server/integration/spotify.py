from api.reddit import get_posts
from integration import get_filtered_posts
from api.spotify import findSong


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
