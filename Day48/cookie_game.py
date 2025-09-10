from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

time.sleep(3)

seconds = 5
timer_check = time.time() + seconds
five_mins = time.time() + 10

try:
    language_button = driver.find_elements(By.CLASS_NAME, "langSelectButton.title")[0]
    language_button.click()
except IndexError:
    print("No language selector")

cookie_button = driver.find_element(By.ID, value="bigCookie")

while True:
    cookie_button.click()

    if time.time() > timer_check:
         
        cookie_counter = int(driver.find_element(By.ID, value="cookies").text.split(" ")[0])
        products = driver.find_elements(By.CLASS_NAME, value="product.unlocked.enabled")
        if not products is None:
            most_expensive_product = products[-1]
            most_expensive_product.click()
        timer_check = time.time() + seconds

    if time.time() >= five_mins:
        break
cookies_per_second=driver.find_element(By.CSS_SELECTOR, value="#cookies div").text.strip().split(":")[1]
print(f"cookies/second = {cookies_per_second}")
driver.close()


