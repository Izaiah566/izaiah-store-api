from models.base import Base
from datetime import datetime

class MessageBase(Base):
    sender_id: int
    receiver_id: int
    content: str

class Message(MessageBase):
    id: int
    created_at: datetime
    is_read: bool = False

    class Config:
        orm_mode = True