from bs4 import BeautifulSoup

with open("./data/081033650810.csv", "r") as f:
    file = f.readlines()

links = [line.rstrip("\n") for line in file]





