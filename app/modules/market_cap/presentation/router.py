from fastapi import APIRouter
from ..application.services import get_market_cap

router = APIRouter()

@router.get("/")
async def market_cap():
    return await get_market_cap()
