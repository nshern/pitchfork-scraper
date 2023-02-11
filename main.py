import requests
from bs4 import BeautifulSoup


def get_album_links():

    counter = 1
    album_links = []

    while True:
    
        params = {"page":counter}
        url = "https://www.pitchfork.com/reviews/albums/"

        response = requests.get(url=url,params=params)

        if response.status_code == 404:
            break

        soup = BeautifulSoup(response.content, "html.parser")

        page_links = [
            link.get("href")
            for link in soup.find_all("a")
            if link.get("href").startswith("/reviews/albums/")
            and "?genre=" not in link.get("href")
            and link.get("href") != "/reviews/albums/"
        ]

        album_links.append(page_links)
        
        print(album_links)

        counter += 1

    
    return album_links


get_album_links()
