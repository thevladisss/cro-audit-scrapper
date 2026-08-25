from fastapi import APIRouter, HTTPException
from app.services.scrapper import scrape
import requests


router = APIRouter(prefix="/scrapper", tags=["scrapper"])

@router.get("/website-snapshot")
def handle_scrape(url: str):
    try:
        return scrape(url)
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=400, detail=str(e))