import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from dotenv import load_dotenv

load_dotenv()


PROMISED_DOWN = 50
PROMISED_UP = 35
TWITTER_EMAIL = os.getenv(key="TWITTER_EMAIL")
TWITTER_PASS = os.getenv(key="TWITTER_PASS")

class InternetSpeedTwitterBot:

    def __init__(self, down, up):
        self._down = down
        self._up = up

    def get_internet_speed(self):
        driver = webdriver.Chrome()
        wait = WebDriverWait(driver=driver, timeout=5)
        driver.get(url="https://www.speedtest.net/")

        policies_button = wait.until(EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler")))
        policies_button.click()

        go_button = driver.find_element(By.CLASS_NAME, value="js-start-test.test-mode-multi")
        go_button.click()
        
        time.sleep(55)

        download_res = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "result-data-large.number.result-data-value.download-speed")))
        upload_res = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "result-data-large.number.result-data-value.upload-speed")))

        download_num = float(download_res.text)
        upload_num = float(upload_res.text)

        print(f"Donwload num:{download_num}, Upload num: {upload_num}")
        return (download_num, upload_num)

    def tweet_at_provider(self, download, upload):
        chrome_options = webdriver.EdgeOptions()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Edge(options=chrome_options)
        wait = WebDriverWait(driver=driver, timeout=10)
        driver.get(url="https://x.com")

        #Main Page
        pollicies_accept_button = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div[2]/button[1]/div")))
        pollicies_accept_button.click()

        sign_in_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[.//span[text()='Sign in']]")))
        sign_in_button.click()

        #Email input + Button
        email_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".r-30o5oe.r-1dz5y72.r-13qz1uu.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-fdjqy7")))
        email_input.send_keys(TWITTER_EMAIL)

        next_button = driver.find_element(By.CSS_SELECTOR, ".r-sdzlij.r-1phboty.r-rs99b7.r-lrvibr.r-ywje51.r-184id4b.r-13qz1uu.r-2yi16.r-1qi8awa.r-3pj75a.r-1loqt21.r-o7ynqc.r-6416eg.r-1ny4l3l")
        next_button.click()

        #Password input + Log In
        pass_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"r-30o5oe.r-1dz5y72.r-13qz1uu.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-fdjqy7")))
        pass_input.send_keys(TWITTER_PASS)

        log_in_button = driver.find_element(By.CSS_SELECTOR, ".css-175oi2r.r-sdzlij.r-1phboty.r-rs99b7.r-lrvibr.r-19yznuf.r-64el8z.r-1fkl15p.r-o7ynqc.r-6416eg.r-icoktb.r-1ny4l3l")
        log_in_button.click()

        time.sleep(10)

internet_bot = InternetSpeedTwitterBot(down=PROMISED_DOWN, up=PROMISED_UP)
# results = internet_bot.get_internet_speed()
internet_bot.tweet_at_provider(PROMISED_DOWN, PROMISED_UP)