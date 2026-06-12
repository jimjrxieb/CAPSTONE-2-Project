"""Small in-process rate limiter for local Eugene API builds."""
from __future__ import annotations

from collections import defaultdict, deque
from time import monotonic

from fastapi import HTTPException


_WINDOW_SECONDS = 60.0
_requests: dict[str, deque[float]] = defaultdict(deque)


def check_rate_limit(user_id: str, *, limit: int) -> None:
    if limit <= 0:
        return
    now = monotonic()
    bucket = _requests[user_id]
    while bucket and now - bucket[0] > _WINDOW_SECONDS:
        bucket.popleft()
    if len(bucket) >= limit:
        raise HTTPException(status_code=429, detail="Query rate limit exceeded")
    bucket.append(now)


def reset_rate_limits() -> None:
    _requests.clear()
