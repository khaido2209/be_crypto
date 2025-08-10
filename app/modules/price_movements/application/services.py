from ..infrastructure.data_provider import fetch_price_movements

async def get_price_movements(top_n: int = 5):
    return await fetch_price_movements(top_n)
