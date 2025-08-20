from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

# -----------------------
# USERS
# -----------------------
class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    password: str  # plain-text for signup; hash it before storing

class User(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


# -----------------------
# CATEGORIES
# -----------------------
class CategoryBase(BaseModel):
    name: str

class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True


# -----------------------
# LISTINGS
# -----------------------
class ListingBase(BaseModel):
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
    created_at: datetime

    class Config:
        orm_mode = True


# -----------------------
# ORDERS
# -----------------------
class OrderBase(BaseModel):
    listing_id: int
    buyer_id: int
    quantity: int = 1

class Order(OrderBase):
    id: int
    order_date: datetime

    class Config:
        orm_mode = True


# -----------------------
# REVIEWS
# -----------------------
class ReviewBase(BaseModel):
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


# -----------------------
# MESSAGES
# -----------------------
class MessageBase(BaseModel):
    sender_id: int
    receiver_id: int
    content: str

class Message(MessageBase):
    id: int
    created_at: datetime
    is_read: bool = False

    class Config:
        orm_mode = True


# -----------------------
# COMMUNITY POSTS
# -----------------------
class PostBase(BaseModel):
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


# -----------------------
# COMMENTS
# -----------------------
class CommentBase(BaseModel):
    comment_text: str

class CommentCreate(CommentBase):
    commenter_id: int

class Comment(CommentBase):
    id: int
    post_id: int
    commenter_id: int
    created_at: datetime

    class Config:
        orm_mode = True
