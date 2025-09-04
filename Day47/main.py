import requests, smtplib, os
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = os.getenv(key="MY_EMAIL")
MY_PASSWORD = os.getenv(key="MY_PASSWORD")
SMTP_ADDRESS = os.getenv(key="SMTP_ADDRESS")



request = requests.get(url="https://desktop.bg/mouse_mats-steelseries-STEELPAD63435")
text = request.text

soup = BeautifulSoup(text, "html.parser")
price_item_text = soup.find("span", class_="bgn").get_text()
price_of_item = float(price_item_text)

target_price = 110

if price_of_item <= target_price:
    with smtplib.SMTP(SMTP_ADDRESS) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        item_name = soup.find(name="h1", itemprop="name").get_text()
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                             msg=f"Subject: Price Change Alert\n\
                             {item_name}The price is {price_of_item}, your target price is {target_price}"
                             )
        connection.close()


