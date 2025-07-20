# app/api/main.py
from fastapi import FastAPI
from app.api.routes import router as api_router

app = FastAPI(title="Eshop Python Modular Mirror")
app.include_router(api_router)

