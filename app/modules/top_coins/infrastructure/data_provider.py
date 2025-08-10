import httpx
from app.core.cache import get_cache, set_cache
from fastapi import HTTPException
import time

COINGECKO_BASE = "https://api.coingecko.com/api/v3"

# Thời gian mặc định chờ lại khi rate limit (giây)
DEFAULT_RETRY_AFTER = 60

async def fetch_top_coins(page: int = 1, per_page: int = 10):
    cache_key = f"top_coins:{page}:{per_page}"
    cached = get_cache(cache_key)
    if cached:
        return cached

    async with httpx.AsyncClient(timeout=10) as client:
        try:
            resp = await client.get(
                f"{COINGECKO_BASE}/coins/markets",
                params={
                    "vs_currency": "usd",
                    "order": "market_cap_desc",
                    "page": page,
                    "per_page": per_page
                }
            )
            resp.raise_for_status()
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 429:
                retry_after = int(e.response.headers.get("Retry-After", DEFAULT_RETRY_AFTER))
                raise HTTPException(
                    status_code=429,
                    detail={
                        "message": "Rate limit exceeded. Please wait before retrying.",
                        "retry_after": retry_after
                    }
                )
            raise

    data = resp.json()
    set_cache(cache_key, data, ttl=60)
    return data
