from fastapi import FastAPI, HTTPException
from app.routers import scrapper

app = FastAPI(
    title="Web Scraper API",
    version="1.0.0",
)

app.include_router(
    scrapper.router,
    prefix="/api/v1",
)
