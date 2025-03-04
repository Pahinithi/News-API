from fastapi import FastAPI
import requests
from pydantic import BaseModel
from typing import List, Optional
from settings import settings


app = FastAPI()


class NewsArticle(BaseModel):
    title: str
    description: Optional[str]
    url: str
    publishedAt: str


def get_news(query: str, page_size: int = 5):
    params = {
        "q": query,
        "pageSize": page_size,
        "apiKey": settings.api_key,
    }
    response = requests.get(settings.base_url, params=params)
    return response.json()


@app.get("/news/sri_lanka", response_model=List[NewsArticle])
async def get_sri_lanka_news(page_size: int = 5):
    news_data = get_news("Sri Lanka", page_size)

    if news_data["status"] == "ok":
        articles = []
        for article in news_data["articles"]:
            articles.append(
                NewsArticle(
                    title=article["title"],
                    description=article.get("description", ""),
                    url=article["url"],
                    publishedAt=article["publishedAt"],
                )
            )
        return articles
    else:
        return {"error": "Unable to fetch news data from NewsAPI"}


@app.get("/news", response_model=List[NewsArticle])
async def get_news_by_query(query: str, page_size: int = 5):
    news_data = get_news(query, page_size)

    if news_data["status"] == "ok":
        articles = []
        for article in news_data["articles"]:
            articles.append(
                NewsArticle(
                    title=article["title"],
                    description=article.get("description", ""),
                    url=article["url"],
                    publishedAt=article["publishedAt"],
                )
            )
        return articles
    else:
        return {"error": "Unable to fetch news data from NewsAPI"}
