from pydantic import BaseModel
from typing import List

class CoinItem(BaseModel):
    id: str
    symbol: str
    name: str
    current_price: float
    market_cap: float
    market_cap_rank: int

class TopCoinsResponse(BaseModel):
    page: int
    per_page: int
    items: List[CoinItem]
