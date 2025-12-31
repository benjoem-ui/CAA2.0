from typing import List
from .reddit_client import get_reddit_readonly
from .models import ThreadCandidate, CollectedBatch


def collect_hot(subreddit: str, limit: int = 25) -> CollectedBatch:
    """
    Collects a small batch of hot posts from a subreddit (read-only).
    No posting, no voting, no messaging.
    """
    reddit = get_reddit_readonly()
    items: List[ThreadCandidate] = []

    for s in reddit.subreddit(subreddit).hot(limit=limit):
        items.append(
            ThreadCandidate(
                subreddit=subreddit,
                post_id=s.id,
                title=s.title,
                url=f"https://www.reddit.com{s.permalink}",
                created_utc=float(s.created_utc),
                score=int(s.score),
                num_comments=int(s.num_comments),
                author=str(s.author) if s.author else None,
            )
        )

    return CollectedBatch(subreddit=subreddit, items=items)
