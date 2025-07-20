from pydantic import BaseModel

class CreateOrderCommand(BaseModel):
    customer_id: int
    product_id: int
    quantity: int
