from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# articles_num = driver.find_elements(By.CSS_SELECTOR, value="#articlecount ul li a")[1].text
# print(articles_num)

driver.get("https://secure-retreat-92358.herokuapp.com/")

fname_bar = driver.find_element(By.NAME, value="fName")
fname_bar.send_keys("Ogi")

lname_bar = driver.find_element(By.NAME, value="lName")
lname_bar.send_keys("Igm")

email_bar = driver.find_element(By.NAME, value="email")
email_bar.send_keys("smthng@gmail")

button = driver.find_element(By.CLASS_NAME, value="btn.btn-lg.btn-primary.btn-block")
button.click()



