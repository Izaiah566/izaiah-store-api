from pydantic import BaseModel
from typing import Optional

class ListingBase(BaseModel):
    title: str
    description: Optional[str] = None
    price: float
    image_url: Optional[str] = None
    category_id: int
    seller_id: int