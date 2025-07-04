import requests
from bs4 import BeautifulSoup

# Target URL
url = "https://books.toscrape.com/"

# Get the webpage
response = requests.get(url)
html = response.text

# Parse HTML
soup = BeautifulSoup(html, "html.parser")

# Extract book titles
books = soup.find_all("h3")

print("Top Books on Home Page:\n")
for book in books:
    title = book.a["title"]
    print("-", title)
