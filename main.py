import uvicorn
from fastapi import FastAPI
from typing import List, Optional

app = FastAPI()

# Mock Data
listings = [
    {"id": 1, "title": "Handmade Ceramic Mug", "price": 18.99, "category": "Home"},
    {"id": 2, "title": "Freelance Logo Design", "price": 75.0, "category": "Design"},
]
categories = ["Home", "Design", "Sports", "Digital"]
reviews = []
messages = []
posts = []
comments = []

# Root
@app.get("/")
async def root():
    return {"message": "Hello World"}

# Test
@app.get("/items")
async def read_items():
    return {"item": "fun"}

# Listings
@app.get("/listings")
async def get_listings():
    return listings

@app.get("/listings/{listing_id}")
async def get_listing(listing_id: int):
    return next((l for l in listings if l["id"] == listing_id), {"error": "Not found"})

@app.post("/listings")
async def create_listing(listing: dict):
    listings.append(listing)
    return listing

@app.put("/listings/{listing_id}")
async def update_listing(listing_id: int, updated: dict):
    for i, l in enumerate(listings):
        if l["id"] == listing_id:
            listings[i].update(updated)
            return listings[i]
    return {"error": "Not found"}

@app.delete("/listings/{listing_id}")
async def delete_listing(listing_id: int):
    global listings
    listings = [l for l in listings if l["id"] != listing_id]
    return {"message": "Deleted"}

# Categories
@app.get("/categories")
async def get_categories():
    return categories

@app.post("/categories")
async def create_category(name: str):
    categories.append(name)
    return {"name": name}

# Reviews
@app.get("/listings/{listing_id}/reviews")
async def get_reviews(listing_id: int):
    return [r for r in reviews if r["listing_id"] == listing_id]

@app.post("/listings/{listing_id}/reviews")
async def add_review(listing_id: int, review: dict):
    review["listing_id"] = listing_id
    reviews.append(review)
    return review

# Messages
@app.get("/messages/{user_id}")
async def get_messages(user_id: int):
    return [m for m in messages if m["to"] == user_id or m["from"] == user_id]

@app.post("/messages")
async def send_message(message: dict):
    messages.append(message)
    return message

# Community Posts
@app.get("/posts")
async def get_posts():
    return posts

@app.get("/posts/{post_id}")
async def get_post(post_id: int):
    return next((p for p in posts if p["id"] == post_id), {"error": "Not found"})

@app.post("/posts")
async def create_post(post: dict):
    posts.append(post)
    return post

# Comments
@app.post("/posts/{post_id}/comments")
async def add_comment(post_id: int, comment: dict):
    comment["post_id"] = post_id
    comments.append(comment)
    return comment

if __name__ == '__main__':
    uvicorn.run('main:app', host='localhost', port=8000, reload=True)
