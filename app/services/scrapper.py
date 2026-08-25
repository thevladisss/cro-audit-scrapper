import requests
from bs4 import BeautifulSoup


def scrape(url: str):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/139.0.0.0 Safari/537.36"
        )
    }

    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.title.string.strip() if soup.title else None

    links = []
    for link in soup.find_all("a", href=True):
        links.append({
            "text": link.get_text(strip=True),
            "url": link["href"]
        })

    return {
        "title": title,
        "links": links,
    }