from ..infrastructure.data_provider import fetch_top_coins

async def get_top_coins(page: int = 1, per_page: int = 10):
    return await fetch_top_coins(page, per_page)
