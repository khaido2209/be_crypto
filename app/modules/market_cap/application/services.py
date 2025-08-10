from ..infrastructure.data_provider import fetch_market_cap

async def get_market_cap():
    return await fetch_market_cap()
