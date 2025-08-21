from models.base import Base
from datetime import datetime

class PostBase(Base):
    title: str
    body: str

class PostCreate(PostBase):
    author_id: int

class Post(PostBase):
    id: int
    author_id: int
    created_at: datetime

    class Config:
        orm_mode = True