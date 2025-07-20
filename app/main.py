# app/main.py
from fastapi import FastAPI
from app.api.routes import router as orders_router

app = FastAPI()

# Include the router from routes.py
app.include_router(orders_router)