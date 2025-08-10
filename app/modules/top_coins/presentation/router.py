from fastapi import APIRouter, Query
from ..application.services import get_top_coins

router = APIRouter()

@router.get("/")
async def top_coins(page: int = Query(1, ge=1), per_page: int = Query(10, le=50)):
    return await get_top_coins(page, per_page)
