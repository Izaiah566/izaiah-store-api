from models.base import Base

class CategoryBase(Base):
    name: str

class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True