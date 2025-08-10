from dataclasses import dataclass
from datetime import datetime

@dataclass
class Alert:
    id: str
    symbol: str
    name: str
    price: float
    change_24h: float
    generated_at: datetime
