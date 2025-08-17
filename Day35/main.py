import requests, smtplib

my_email = ":)"
my_password = ":)"


my_url = "https://api.openweathermap.org/data/2.5/forecast"

parameters ={ 
    "lat" : 43.4167,
    "lon" : 24.6167,
    "cnt" : 4,
    "appid" : "....",
}

request = requests.get(url=my_url,
                        params=parameters)
request.raise_for_status()
weather_data = request.json()

weather_info_hours = weather_data["list"]

for i in weather_info_hours:
    weather_info_hour_id = i["weather"][0]["id"]
    if weather_info_hour_id < 700:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=my_email,
                                 msg=f"Subject:Hello\nIt is going to rain.\nBring an umbrella.")
            connection.close()
        break

