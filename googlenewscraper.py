import requests
from bs4 import BeautifulSoup


def get_top_news(location):
    base_url = "https://news.google.com/"
    search_url = base_url + f"search?q={location}+deforestation&hl=en-US&gl=US&ceid=US%3Aen"

    response = requests.get(search_url)
    soup = BeautifulSoup(response.content, "html.parser")

    articles = soup.select(".NiLAwe")[:5]  # Limit to top 5 articles
    news = {}
    for article in articles:
        title = article.select_one("h3 > a").text.strip()
        link = article.select_one("h3 > a")["href"]
        if not link.startswith("http"):
            link = base_url + link[2:]
        summary_elem = article.select_one("article > div:last-of-type")
        
        img_elem = article.select_one("img")
        if img_elem:
            img = img_elem["src"]
        else:
            img = "No image available"
        news[title] = {"link": link, "img": img}
    return news
