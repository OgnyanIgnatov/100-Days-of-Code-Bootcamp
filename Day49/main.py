from selenium import webdriver
from selenium.webdriver.common.by import By
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")