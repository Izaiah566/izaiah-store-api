from pydantic import BaseModel
from datetime import datetime

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