import httpx
from app.core.cache import get_cache, set_cache

COINGECKO_BASE = "https://api.coingecko.com/api/v3"

async def fetch_price_movements(top_n: int = 5):
    cache_key = f"price_movements:{top_n}"
    cached = get_cache(cache_key)
    if cached:
        return cached

    async with httpx.AsyncClient(timeout=10) as client:
        resp = await client.get(
            f"{COINGECKO_BASE}/coins/markets",
            params={
                "vs_currency": "usd",
                "order": "market_cap_desc",
                "per_page": 100,
                "page": 1
            }
        )
        resp.raise_for_status()
        coins = resp.json()

    top_gainers = sorted(coins, key=lambda c: c.get("price_change_percentage_24h", 0) or 0, reverse=True)[:top_n]
    top_losers = sorted(coins, key=lambda c: c.get("price_change_percentage_24h", 0) or 0)[:top_n]

    data = {"top_gainers": top_gainers, "top_losers": top_losers}
    set_cache(cache_key, data, ttl=60)
    return data
