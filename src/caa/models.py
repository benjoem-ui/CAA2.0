from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class ThreadCandidate(BaseModel):
    subreddit: str
    post_id: str
    title: str
    url: str
    created_utc: float
    score: int
    num_comments: int
    author: Optional[str] = None


class CollectedBatch(BaseModel):
    collected_at: datetime = Field(default_factory=datetime.utcnow)
    subreddit: str
    items: List[ThreadCandidate]
