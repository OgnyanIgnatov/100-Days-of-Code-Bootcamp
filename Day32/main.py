import random, smtplib, datetime as dt

my_email = ":)"
password = ":) :) :)"

date = dt.datetime.now()

if date.weekday() == 1:
    with open("quotes.txt") as file:
        data = file.readlines()

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=":)", 
                            msg=f"Subject:Hello\n\n{random.choice(data)}")
        connection.close()


