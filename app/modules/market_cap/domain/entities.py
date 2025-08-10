from dataclasses import dataclass
from datetime import datetime

@dataclass
class MarketCap:
    active_cryptocurrencies: int
    total_market_cap_usd: float
    updated_at: datetime
