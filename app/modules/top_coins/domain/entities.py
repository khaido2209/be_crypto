from dataclasses import dataclass

@dataclass
class Coin:
    id: str
    symbol: str
    name: str
    current_price: float
    market_cap: float
    market_cap_rank: int
