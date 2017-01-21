from praw.models import Submission
from api.reddit import get_posts


def _filter_post(post):
    """
    Return true if post should be kept as a possible music track.
    :type post Submission
    :rtype bool
    """

    return True


def _filter_posts(posts):
    """
    Return all posts that meet filter condition.
    :param posts:
    :rtype list[Submission]
    """

    return filter(_filter_post, posts)


def get_filtered_posts(subreddit):
    """
        Return all posts from subreddit that meet filter condition.
        :param posts:
        :rtype list[Submission]
        """

    return _filter_posts(get_posts(subreddit))
