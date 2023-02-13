from pathlib import Path
import requests
from bs4 import BeautifulSoup
import csv
import os

def get_album_links():
    
    data_folder = f"{os.getcwd()}/data/"
    if not Path(data_folder).exists():
        os.mkdir(data_folder)

    counter = 1
    album_links = []
    retries = 10
    s = requests.Session()

    while retries > 0 and counter < 100:
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

    flat_list = [item for sublist in album_links for item in sublist]

    return flat_list

if __name__ == "__main__":
    from datetime import datetime

    file_name = f'{os.getcwd()}/data/{datetime.now().strftime("%H%M%S%f")}.csv'

    l = get_album_links()

    for i in l:
        with open(file_name, "a") as f:
            f.write(f"{i}\n")

