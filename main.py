import requests
from bs4 import BeautifulSoup

url = "https://www.pitchfork.com/reviews/albums/"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

album_links = [
    link.get("href")
    for link in soup.find_all("a")
    if link.get("href").startswith("/reviews/albums/")
    and "?genre=" not in link.get("href")
    and link.get("href") != "/reviews/albums/"
]

for i in album_links:
    print(i)
