import os
import praw


def get_reddit_readonly() -> praw.Reddit:
    """
    Returns a read-only Reddit client.
    Requires environment variables:
      REDDIT_CLIENT_ID
      REDDIT_CLIENT_SECRET
      REDDIT_USER_AGENT
    """
    client_id = os.environ.get("REDDIT_CLIENT_ID", "").strip()
    client_secret = os.environ.get("REDDIT_CLIENT_SECRET", "").strip()
    user_agent = os.environ.get("REDDIT_USER_AGENT", "").strip()

    if not client_id or not client_secret or not user_agent:
        raise RuntimeError(
            "Missing Reddit credentials. Set REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, and REDDIT_USER_AGENT."
        )

    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent,
    )
    reddit.read_only = True
    return reddit
