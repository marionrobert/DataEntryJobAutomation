import requests
import os
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

form_link = "https://docs.google.com/forms/d/e/1FAIpQLScpugvfEwpdubyVqhZoaErEUoWvlT63MH6fmHpzn6TAD1l2fg/viewform?usp=sf_link"
zillow_search_URL = "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A37.92845633054633%2C%22east%22%3A-122.16347781542969%2C%22south%22%3A37.62180960547711%2C%22west%22%3A-122.70318118457031%7D%2C%22mapZoom%22%3A11%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"

chrome_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7"
}

edge_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44",
    "Accept-Language": "fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"
}

response = requests.get(zillow_search_URL, headers=edge_headers)
time.sleep(5)
# print(response.status_code)
web_data = response.content
soup = BeautifulSoup(web_data, "html.parser")
# print(soup.prettify())

# find all links
original_links = soup.find_all("a", class_="property-card-link")
all_links = [f"https://www.zillow.com{link.get('href')}" for link in original_links]
# print(all_links)

# find all prices
original_prices = soup.select("div.property-card-data span.keDkae")
all_prices = [int(price.text.split("+")[0].split("/mo")[0].replace("$", "").replace(",", "")) for price in original_prices]
# print(all_prices)

# find all_addresses
original_addresses = soup.find_all("address")
all_addresses = [address.text for address in original_addresses]
# print(all_addresses)

# open the form page with selenium
chrome_driver_path = os.environ["CHROME_DRIVER_PATH"]
service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)

# for each appartment, fill in the form
for n in range(len(all_prices)):
    driver.get(form_link)
    time.sleep(3)
    print(f"-- Appartment n°{n+1} --")
    print("find_input_address and write address")
    input_address = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    input_address.send_keys(all_addresses[n])
    time.sleep(3)
    print("find_input_price and write price")
    input_address = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    input_address.send_keys(all_prices[n])
    time.sleep(3)
    print("find_input_link and write link")
    input_address = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    input_address.send_keys(all_links[n])
    time.sleep(3)
    print("send the form")
    send_button = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span")
    send_button.click()
