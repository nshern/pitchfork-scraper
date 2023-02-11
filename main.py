from pathlib import Path
import requests
from bs4 import BeautifulSoup

def get_album_links(file):
    path = Path(file)
    if path.exists():
        db = pd.read_csv(path)
        existing_links = db["links"] 

    counter = 1
    album_links = []
    retries = 10
    s = requests.Session()

    while retries > 0:
        print(counter)
    
        params = {"page":counter}
        url = "https://www.pitchfork.com/reviews/albums/"

        try:
            response = s.get(url=url,params=params,timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "html.parser")

            page_links = [
            link.get("href")
            for link in soup.find_all("a")
            if link.get("href").startswith("/reviews/albums/")
            and "?genre=" not in link.get("href")
            and link.get("href") != "/reviews/albums/"
            ]

            album_links.append(page_links)
            

            counter += 1


        except requests.exceptions.RequestException as ex:
            if response.status_code == 404:
                print("reached end of the line")
                break
            else:
                print(ex)
                print("retrying...")
                retries -= 1


    return album_links

if __name__ == "__main__":
    import pandas as pd

    #links = get_album_links()

    links = [item for sublist in get_album_links() for item in sublist]

    df = pd.DataFrame()

    df["links"] = links

    df.to_csv("df.csv")




