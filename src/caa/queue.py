import csv
from pathlib import Path
from .models import CollectedBatch


def write_batch_to_csv(batch: CollectedBatch, out_path: str) -> str:
    """
    Writes collected candidates to a CSV queue file.
    This is intentionally simple for MVP and review.
    """
    path = Path(out_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["subreddit", "post_id", "title", "url", "created_utc", "score", "num_comments", "author"])
        for item in batch.items:
            w.writerow([
                item.subreddit,
                item.post_id,
                item.title,
                item.url,
                item.created_utc,
                item.score,
                item.num_comments,
                item.author or "",
            ])

    return str(path)
