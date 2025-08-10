from dataclasses import dataclass

@dataclass
class Movement:
    id: str
    symbol: str
    name: str
    price_change_percentage_24h: float
    current_price: float
