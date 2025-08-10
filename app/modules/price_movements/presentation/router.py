from fastapi import APIRouter, Query
from ..application.services import get_price_movements

router = APIRouter()

@router.get("/")
async def price_movements(top_n: int = Query(5, ge=1, le=20)):
    return await get_price_movements(top_n)
