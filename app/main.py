# Main application entry point implementing a modular FastAPI service
# Architecture follows Clean Architecture principles with:
# - Presentation layer (routers)
# - Application layer (services)
# - Domain layer (entities)
# - Infrastructure layer (data providers)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.modules.top_coins.presentation.router import router as top_coins_router
from app.modules.price_movements.presentation.router import router as price_movements_router
from app.modules.alerts.presentation.router import router as alerts_router
from app.modules.market_cap.presentation.router import router as market_cap_router

app = FastAPI(title="Modular Dashboard API - Crypto Widgets")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(top_coins_router, prefix="/api/top-coins", tags=["top-coins"])
app.include_router(price_movements_router, prefix="/api/price-movements", tags=["price-movements"])
app.include_router(alerts_router, prefix="/api/alerts", tags=["alerts"])
app.include_router(market_cap_router, prefix="/api/market-cap", tags=["market-cap"])

@app.get("/")
async def root():
    return {"status": "ok"}
