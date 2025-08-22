import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASS = os.getenv("MY_PASSWORD")



class NotificationManager:
    pass
    
def send_message(users_data, cheapest_flight,dep_city, destination, dep_date, arr_date):
     with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASS)
        for user in users_data:
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=user,
                                msg=f"Subject:Cheap Flight\n"+
                                f"GBP{cheapest_flight}\n" + 
                                f"{dep_city}\n" + 
                                f"{destination}\n" + 
                                f"{dep_date}\n" +
                                f"{arr_date}" 
                                )
        connection.close()