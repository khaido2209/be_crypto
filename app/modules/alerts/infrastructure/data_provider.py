import httpx
from app.core.cache import get_cache, set_cache

COINGECKO_BASE = "https://api.coingecko.com/api/v3"

async def fetch_alerts(threshold_pct: float = 5.0, per_page: int = 50):
    cache_key = f"alerts:{threshold_pct}:{per_page}"
    cached = get_cache(cache_key)
    if cached:
        return cached

    async with httpx.AsyncClient(timeout=10) as client:
        resp = await client.get(
            f"{COINGECKO_BASE}/coins/markets",
            params={
                "vs_currency": "usd",
                "order": "market_cap_desc",
                "per_page": per_page,
                "page": 1
            }
        )
        resp.raise_for_status()
        coins = resp.json()

    alerts = [
        {
            "id": c["id"],
            "symbol": c["symbol"],
            "name": c["name"],
            "price": c["current_price"],
            "change_24h": c["price_change_percentage_24h"]
        }
        for c in coins if abs(c.get("price_change_percentage_24h", 0) or 0) >= threshold_pct
    ]

    data = {"alerts": alerts}
    set_cache(cache_key, data, ttl=60)
    return data
