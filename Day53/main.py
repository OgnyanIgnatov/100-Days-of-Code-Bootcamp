import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSeZyXKu2MtOvAE2GAkgeIkvyn0jq0sfG9H4OIRftzxnaIlj9g/viewform?usp=dialog"

request = requests.get(url="https://appbrewery.github.io/Zillow-Clone/")
data = request.text

soup = BeautifulSoup(data, "html.parser")
listings = soup.find_all(name="li", class_="ListItem-c11n-8-84-3-StyledListCardWrapper")

address_list = []
links_list = []
prices_list = []

for listing in listings:
    address = listing.select(selector="div div article div div a address")[0].get_text().strip()
    price = listing.select(selector="div div article div div div div span")[0].get_text()[:6]
    link = listing.select(selector="div div article div div a")[0].get("href").strip()

    address_list.append(address)
    prices_list.append(price)
    links_list.append(link)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(url=FORM_URL)

for i in range(len(address_list)):
    time.sleep(5)
    address_inputs = driver.find_elements(By.CSS_SELECTOR, value=".whsOnd.zHQkBf")
    address_inputs[0].send_keys(address_list[i])
    address_inputs[1].send_keys(prices_list[i])
    address_inputs[2].send_keys(links_list[i])
    time.sleep(1)
    send_button = driver.find_element(By.CSS_SELECTOR, value=".NPEfkd.RveJvd.snByac")
    send_button.click()
    time.sleep(3)
    send_another_response_link = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
    send_another_response_link.click()
    
    




