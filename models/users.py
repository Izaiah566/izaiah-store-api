from pydantic import EmailStr
from models.base import Base
from datetime import datetime

# -----------------------
# USERS
# -----------------------
class UserBase(Base):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    password: str  # plain-text for signup; hash it before storing

class User(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True