import praw
from globals import REDDIT_USER_AGENT, REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET

reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID, client_secret=REDDIT_CLIENT_SECRET, user_agent=REDDIT_USER_AGENT)


def get_posts(subreddit):
    """
    Return posts in subreddit.
    :type subreddit: str
    :rtype list
    """

    return [
        submission
        for submission
        in reddit.subreddit(subreddit).hot(limit=100)
    ]
