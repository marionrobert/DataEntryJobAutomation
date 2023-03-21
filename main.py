import requests
import os
from bs4 import BeautifulSoup
import lxml

form_link = "https://docs.google.com/forms/d/e/1FAIpQLScpugvfEwpdubyVqhZoaErEUoWvlT63MH6fmHpzn6TAD1l2fg/viewform?usp=sf_link"
zillow_search_URL = "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A37.85381150365383%2C%22east%22%3A-122.29840365771484%2C%22south%22%3A37.69668892292081%2C%22west%22%3A-122.56825534228516%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%7D"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7"
}

response = requests.get(zillow_search_URL, headers=headers)
# print(response.status_code)
web_data = response.content

# soup = BeautifulSoup(web_data, "html.parser")
soup = BeautifulSoup(web_data, parser=lxml, features="lxml")
# print(soup.prettify())

# https://www.zillow.com +/b/parkmerced-san-francisco-ca-5XjKHx/

original_links = soup.find_all("a", class_="property-card-link")
all_links = [f"https://www.zillow.com{link.get('href')}" for link in original_links]
print(all_links)