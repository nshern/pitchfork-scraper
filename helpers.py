from pathlib import Path
import requests
from bs4 import BeautifulSoup
import os
import time
import hashlib


def get_album_links():

    data_folder = f"{os.getcwd()}/data/"
    if not Path(data_folder).exists():
        os.mkdir(data_folder)

    counter = 1
    album_links = []
    retries = 10
    s = requests.Session()

    while retries > 0:
        if counter % 2 == 0:
            print(f"scraping page {counter}..")
        else:
            print(f"scraping page {counter}...")

        params = {"page": counter}
        url = "https://www.pitchfork.com/reviews/albums/"

        try:
            response = s.get(url=url, params=params, timeout=10)
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
                print("reached end of the line!")
                break
            else:
                print(ex)
                print("retrying...")
                retries -= 1
                time.sleep(10)

        finally:
            os.system("clear")

    flat_list = [item for sublist in album_links for item in sublist]

    return flat_list

def string_to_sha1(string):

    return hashlib.sha1(string)


def write_soup_to_html(soup, directory):

    with open(directory, "w") as f:
        f.write(soup.prettify())
    

def get_album_scores(link, session):

    try:
        response = session.get(link)
        response.raise_for_status()
        
    except: 
        raise Exception

    print(response.status_code)
    soup = BeautifulSoup(response.content,"html.parser")
    
    scores = soup.find_all("span", {"class":"score"})

    return [i.text for i in scores]

if __name__ == "__main__":
    pass
    
   # with open("./data/081033650810.csv") as f:
   #     links = f.readlines()
   # 
   # links = [line.rstrip("\n") for line in links]

   # s = requests.Session()

   # for link in links[:10]:
   #     link = f"https://www.pitchfork.com{link}"
   #     print(get_album_scores(link=link,session=s))
        


#    for link in links:
#        response = requests.get(f"https://www.pitchfork.com/{link}",timeout=5)
#
#        soup = BeautifulSoup(response.content,"html.parser")
#
#        scores = soup.find_all("span", {"class":"score"})
#
#        if len(scores) != 1:
#            pass
#            # do something to handle mutiple scores
#            
#
