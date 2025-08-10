from pydantic import BaseModel
from datetime import datetime

class MarketCapResponse(BaseModel):
    active_cryptocurrencies: int
    total_market_cap_usd: float
    updated_at: datetime
