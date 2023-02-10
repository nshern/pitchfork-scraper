import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup


def get_album_links():

    url = "https://www.pitchfork.com/reviews/albums/"
    
   # pitchfork_adapter = HTTPAdapter(max_retries=3)
   # session = requests.session()

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


