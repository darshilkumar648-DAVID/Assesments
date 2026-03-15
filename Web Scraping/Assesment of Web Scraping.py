import requests
from bs4 import BeautifulSoup as soup
import pandas as pd

url = "http://quotes.toscrape.com/"
web = requests.get(url)

web

soup = soup(web.content, "html.parser")

quotes = []
for quote in soup.find_all("span",class_="text"):
  quotes.append(quote.text)

authors = []
for author in soup.find_all("small",class_="author"):
  authors.append(author.text)

df = pd.DataFrame({"Quotes": quotes,"Authors": authors})
df.to_excel("quotes_data.xlsx", index=False)
print(df)