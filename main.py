import uvicorn
from fastapi import FastAPI, HTTPException
from supabase import create_client, Client
from dotenv import load_dotenv
from fastapi.encoders import jsonable_encoder
import os

from models.users import User, UserBase, UserCreate
from models.categories import CategoryBase, Category
from models.listings import ListingBase, ListingCreate, Listing
from models.orders import Order, OrderBase
from models.reviews import Review, ReviewBase, ReviewCreate
from models.messages import Message, MessageBase
from models.community_posts import Post, PostBase, PostCreate
from models.comments import Comment, CommentBase, CommentCreate

# Load env variables
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Marketplace API with Supabase"}

# -----------------------
# LISTINGS
# -----------------------
@app.get("/listings", response_model=list[Listing])
async def get_listings():
    result = supabase.table("listings").select("*").execute()
    print(result)  # log the raw response
    return result.data


@app.get("/listings/{listing_id}", response_model=Listing)
async def get_listing(listing_id: int):
    data = supabase.table("listings").select("*").eq("id", listing_id).execute()
    if not data.data:
        raise HTTPException(status_code=404, detail="Listing not found")
    return jsonable_encoder(data.data[0])

@app.post("/listings")
async def create_listing(listing: dict):
    data = supabase.table("listings").insert(listing).execute()
    return data.data

@app.put("/listings/{listing_id}")
async def update_listing(listing_id: int, updates: dict):
    data = supabase.table("listings").update(updates).eq("id", listing_id).execute()
    return data.data

@app.delete("/listings/{listing_id}")
async def delete_listing(listing_id: int):
    supabase.table("listings").delete().eq("id", listing_id).execute()
    return {"message": "Listing deleted"}

# -----------------------
# CATEGORIES
# -----------------------
@app.get("/categories")
async def get_categories():
    data = supabase.table("categories").select("*").execute()
    return data.data

@app.post("/categories")
async def create_category(category: dict):
    data = supabase.table("categories").insert(category).execute()
    return data.data

# -----------------------
# REVIEWS
# -----------------------
@app.get("/listings/{listing_id}/reviews")
async def get_reviews(listing_id: str):
    data = supabase.table("reviews").select("*").eq("listing_id", listing_id).execute()
    return data.data

@app.post("/listings/{listing_id}/reviews")
async def add_review(listing_id: str, review: dict):
    review["listing_id"] = listing_id
    data = supabase.table("reviews").insert(review).execute()
    return data.data

# -----------------------
# MESSAGES
# -----------------------
@app.get("/messages/{user_id}")
async def get_messages(user_id: str):
    data = supabase.table("messages").select("*").or_(f"sender_id.eq.{user_id},receiver_id.eq.{user_id}").execute()
    return data.data

@app.post("/messages")
async def send_message(message: dict):
    data = supabase.table("messages").insert(message).execute()
    return data.data

# -----------------------
# COMMUNITY POSTS
# -----------------------
@app.get("/posts")
async def get_posts():
    data = supabase.table("community_posts").select("*").execute()
    return data.data

@app.get("/posts/{post_id}")
async def get_post(post_id: str):
    post = supabase.table("community_posts").select("*").eq("id", post_id).execute()
    if not post.data:
        raise HTTPException(status_code=404, detail="Post not found")
    return post.data[0]

@app.post("/posts")
async def create_post(post: dict):
    data = supabase.table("community_posts").insert(post).execute()
    return data.data

# -----------------------
# COMMENTS
# -----------------------
@app.post("/posts/{post_id}/comments")
async def add_comment(post_id: str, comment: dict):
    comment["post_id"] = post_id
    data = supabase.table("comments").insert(comment).execute()
    return data.data

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
