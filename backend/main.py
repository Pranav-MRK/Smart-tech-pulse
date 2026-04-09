from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from app.service.news_service import fetch_news, filter_news_by_interests
from app.service.llm_service import generate_summary
from app.service.vector_service import store_news,query_news

app = FastAPI()

class UserRequest(BaseModel):
    email: str
    interests: List[str]

@app.post("/generate-news")
def generate_news(user: UserRequest):
    # Step 1: Fetch news
    news = fetch_news()
    # Step 2: Store in vector DB
    store_news(news)
    # Step 3: Retrieve relevant news
    relevant_news = query_news(user.interests)
    # Step 4: Send to LLM
    summary = generate_summary(
        [{"title": n, "summary": ""} for n in relevant_news],
        user.interests
    )

    return {
        "user": user,
        "retrieved_news": relevant_news,
        "summary": summary
    }