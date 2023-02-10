
import requests
from bs4 import BeautifulSoup
import csv

# Set the URL that you want to scrape
url = "https://pitchfork.com/reviews/albums/ab-soul-herbert/"

# Make a request to the website
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, "html.parser")

# Find the review div on the page
review_div = soup.find("div", class_="review__body")

# Find the review text
review_text = review_div.find("div", class_="review__text").text.strip()

# Create a CSV file to store the data
with open("review.csv", "w", newline="") as csv_file:
    # Create a CSV writer
    writer = csv.writer(csv_file)
    # Write the header row
    writer.writerow(["review_text"])
    # Write the review text to the CSV file
    writer.writerow([review_text])
