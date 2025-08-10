import httpx
from datetime import datetime
from app.core.cache import get_cache, set_cache

COINGECKO_BASE = "https://api.coingecko.com/api/v3"

async def fetch_market_cap():
    cache_key = "market_cap"
    cached = get_cache(cache_key)
    if cached:
        return cached

    async with httpx.AsyncClient(timeout=10) as client:
        resp = await client.get(f"{COINGECKO_BASE}/global")
        resp.raise_for_status()
        global_data = resp.json().get("data", {})

    data = {
        "active_cryptocurrencies": global_data.get("active_cryptocurrencies"),
        "total_market_cap_usd": global_data.get("total_market_cap", {}).get("usd"),
        "updated_at": datetime.utcnow().isoformat()
    }
    set_cache(cache_key, data, ttl=60)
    return data
