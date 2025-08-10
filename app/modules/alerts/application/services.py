from ..infrastructure.data_provider import fetch_alerts

async def get_alerts(threshold_pct: float = 5.0, per_page: int = 50):
    return await fetch_alerts(threshold_pct, per_page)
