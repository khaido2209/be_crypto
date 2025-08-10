from pydantic import BaseModel
from typing import List

class MovementItem(BaseModel):
    id: str
    symbol: str
    name: str
    price_change_percentage_24h: float
    current_price: float

class PriceMovementsResponse(BaseModel):
    top_gainers: List[MovementItem]
    top_losers: List[MovementItem]
