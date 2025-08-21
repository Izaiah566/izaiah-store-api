from models.base import Base
from typing import Optional
from datetime import datetime

class ListingBase(Base):
    title: str
    description: Optional[str] = None
    price: float
    image_url: Optional[str] = None
    category_id: int
    seller_id: int

class ListingCreate(ListingBase):
    pass

class Listing(ListingBase):
    id: int
    created_at: Optional[str]

    class Config:
        orm_mode = True