##################### Extra Hard Starting Project ######################
import pandas, datetime as dt, random, smtplib

data = pandas.read_csv("./Birthday Wisher/birthdays.csv")
data_dict = data.to_dict(orient="records")

today = dt.datetime.now()

for person in data_dict:
    if person["month"] == today.month and person["day"] == today.day:
        letter_number = random.choice(range(1,4))

        with open(f"./Birthday Wisher/letter_templates/letter_{letter_number}.txt") as file:
            letter = file.read()
            letter = letter.replace("[NAME]", person["name"])
        
        my_email = ":)"
        password = ":) :) :)"
        
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(my_email, person["email"], msg=f"Subject:HAPPY BIRTHDAY\n\n{letter}")
            connection.close()




