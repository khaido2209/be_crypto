from pydantic import BaseModel
from typing import List
from datetime import datetime

class AlertItem(BaseModel):
    id: str
    symbol: str
    name: str
    price: float
    change_24h: float
    generated_at: datetime

class AlertsResponse(BaseModel):
    alerts: List[AlertItem]
