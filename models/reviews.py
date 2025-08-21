from models.base import Base
from sqlmodel import Field
from typing import Optional
from datetime import datetime

class ReviewBase(Base):
    rating: int = Field(..., ge=1, le=5)
    review_text: Optional[str] = None

class ReviewCreate(ReviewBase):
    reviewer_id: int

class Review(ReviewBase):
    id: int
    listing_id: int
    reviewer_id: int
    created_at: datetime

    class Config:
        orm_mode = True