from fastapi import APIRouter
from app.application.commands.create_order import CreateOrderCommand
from app.application.handlers.create_order_handler import CreateOrderHandler

router = APIRouter()

@router.post("/orders")
def create_order(cmd: CreateOrderCommand):
    handler = CreateOrderHandler()
    result = handler.handle(cmd)
    return result