from selenium import webdriver
from selenium.webdriver.common.by import By

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)


# driver = webdriver.Chrome(options=chrome_options)
# driver.get(url="https://desktop.bg/mouse_mats-cougar-CG3MARENAX0001")
# price = driver.find_element(By.CLASS_NAME,value="bgn").text
# print(price)

# driver.quit()

driver = webdriver.Chrome()
driver.get(url="https://www.python.org/")

upc_events = driver.find_elements(By.CSS_SELECTOR,".medium-widget.event-widget.last li")

container=dict()
for index,el in enumerate(upc_events):
    date = el.find_element(By.TAG_NAME, value="time").text
    event_name = el.find_element(By.TAG_NAME, value="a").text
    container[index] = {"time" : date,""
                        "name" : event_name}
    
print(container)
