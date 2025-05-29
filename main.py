from fastapi import FastAPI
from api import buyer, seller, admin  # пока не создавали, просто для структуры
#from session import engine  # подключение к БД, позже добавим
from models import base  # для Alembic

app = FastAPI(
    title="Marketplace",
    description="Продажа смартфонов и аксессуаров",
    version="0.1.0"
)

# Подключаем роутеры
#app.include_router(buyer.router, prefix="/buyer", tags=["Buyer"])
#app.include_router(seller.router, prefix="/seller", tags=["Seller"])
#app.include_router(admin.router, prefix="/admin", tags=["Admin"])
