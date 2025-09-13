from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

ACCOUNT_MAIL = "ognyan@test.com"
PASSWORD = "3J7bLQfRpiU5b5K"

def login(mail : str, passw: str, driver : webdriver.Chrome) -> None:
    wait = WebDriverWait(driver, timeout=3)


    login_button = wait.until(EC.presence_of_element_located((By.ID, "login-button")))
    login_button.click()

    email_input = wait.until(EC.presence_of_element_located((By.ID, "email-input")))
    password_input = wait.until(EC.presence_of_element_located((By.ID, "password-input")))
    submit_button = wait.until(EC.presence_of_element_located((By.ID, "submit-button")))

    
    email_input.send_keys(mail)
    password_input.send_keys(passw)
    submit_button.click()

    wait.until(EC.presence_of_element_located((By.ID, "schedule-page")))

def verify(driver:webdriver.Chrome, counter = int) -> None:
    wait = WebDriverWait(driver, timeout=5)

    my_bookings_button = driver.find_element(By.ID, value="my-bookings-link")
    my_bookings_button.click()

    try:
        bookings_section = driver.find_element(By.ID, "confirmed-bookings-section")
        bookings_count = len(bookings_section.find_elements(By.CSS_SELECTOR, "div[id^='booking-card-booking_']"))
    except:
        bookings_count = 0

    try:
        waitlisted_section = driver.find_element(By.ID, "waitlist-section")
        waitlist_count = len(waitlisted_section.find_elements(By.CSS_SELECTOR, "div[id^='waitlist-card-waitlist_']"))
    except:
        waitlist_count = 0

    if not bookings_count + waitlist_count == counter:
        print(f"---VERIFICATIONS RESULT---\n\
            Expected: {counter}\n\
            Found: {bookings_count + waitlist_count}\n\
            Missmatch: {abs(bookings_count + waitlist_count - counter)}") 
    else:
        print(f"---VERIFICATIONS RESULT---\n\
            Expected: {counter}\n\
            Found: {bookings_count + waitlist_count}\n\
            Success: All bookings verified") 



def book_class(driver:webdriver.Chrome) -> None:

    class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")
    waitlist_counter,book_counter, booked_or_waitlisted_counter,  = 0,0,0

    for card in class_cards:
        # Get the day title from the parent day group
        day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
        day_title = day_group.find_element(By.TAG_NAME, "h2").text

        if "Tue" in day_title or "Thu" in day_title:
            # Check if this is a 6pm class
            time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
            if "6:00 PM" in time_text:
                # Get the class name
                class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text

                # Find and click the book button
                button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")
                
                
                if button.text == "Book Class":
                    button.click()
                    book_counter+=1
                    print(f"Booked: {class_name} on {day_title}")
                    time.sleep(0.5)
                elif button.text == "Booked":
                    booked_or_waitlisted_counter+=1
                    print(f"Already booked:{class_name} on {day_title}")
                    time.sleep(0.5)
                elif button.text == "Waitlisted":
                    booked_or_waitlisted_counter+=1
                    print(f"Already on waitlist: {class_name} on {day_title}")
                    time.sleep(0.5)
                elif button.text == "Join Waitlist":
                    button.click()
                    waitlist_counter+=1
                    print(f"Joined waitlist for: {class_name} on {day_title}")
                    time.sleep(0.5)

    sum_of_counters = book_counter + waitlist_counter + booked_or_waitlisted_counter
    
    print(f"""
        ---Booking Summary---
        Classes booked: {book_counter}
        Waitlists joined: {waitlist_counter}
        Already booked/waitlisted {booked_or_waitlisted_counter}
        Total Tuesday and Thursday booked classes: {sum_of_counters}
    """)
    verify(driver, sum_of_counters)
                
    
def main():

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
    try:
        os.mkdir(user_data_dir)
    except FileExistsError:
        pass
    chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

    driver = webdriver.Chrome(options=chrome_options)


    driver.get("https://appbrewery.github.io/gym/")
    login(ACCOUNT_MAIL,PASSWORD, driver)
    book_class(driver)

main()



