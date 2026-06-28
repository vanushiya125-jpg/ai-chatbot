import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

quotes = []
authors = []

for quote in soup.find_all("div", class_="quote"):
    quotes.append(quote.find("span", class_="text").text)
    authors.append(quote.find("small", class_="author").text)

data = pd.DataFrame({
    "Quote": quotes,
    "Author": authors
})

data.to_csv("quotes_data.csv", index=False)

print("Web Scraping Completed Successfully!")
print(data)
