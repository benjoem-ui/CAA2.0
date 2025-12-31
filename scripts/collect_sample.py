import os
from dotenv import load_dotenv

from caa.collector import collect_hot
from caa.queue import write_batch_to_csv


def main():
    load_dotenv()

    subreddit = os.environ.get("TARGET_SUBREDDIT", "entrepreneur")
    batch = collect_hot(subreddit=subreddit, limit=15)

    out_file = f"queue/{subreddit}_hot.csv"
    saved = write_batch_to_csv(batch, out_file)

    print(f"Collected {len(batch.items)} posts from r/{subreddit}")
    print(f"Wrote queue file: {saved}")


if __name__ == "__main__":
    main()
