# app/domain/order.py

from dataclasses import dataclass

@dataclass
class Order:
    id: int
    item: str
    quantity: int
