from fastapi import APIRouter, Query
from ..application.services import get_alerts

router = APIRouter()

@router.get("/")
async def alerts(threshold_pct: float = Query(5.0), per_page: int = Query(50, le=100)):
    return await get_alerts(threshold_pct, per_page)
