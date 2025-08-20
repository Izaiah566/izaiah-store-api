from pydantic import BaseModel
from datetime import datetime

class OrderBase(BaseModel):
    listing_id: int
    buyer_id: int
    quantity: int = 1

class Order(OrderBase):
    id: int
    order_date: datetime

    class Config:
        orm_mode = True
        