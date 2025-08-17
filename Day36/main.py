import requests, datetime as dt, json, smtplib
from tkinter import messagebox


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "..."
NEWS_API_KEY = "..."
MY_EMAIL = ":)"
MY_PASS = ":)"


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
news_url = f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&apiKey={STOCK_API_KEY}"

stock_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={STOCK_API_KEY}"
stock_request = requests.get(url=stock_url)
stock_data = stock_request.json()["Time Series (Daily)"]

try:
    price_of_yesterday = float(stock_data[str(dt.datetime.now().date() - dt.timedelta(days=2))]["4. close"])
    price_of_day_before = float(stock_data[str(dt.datetime.now().date() - dt.timedelta(days=3))]["4. close"])
except KeyError:
    messagebox.showerror(message="Invalid Key")
else:

    difference = price_of_yesterday - price_of_day_before
    percent_change = (difference / price_of_day_before) * 100
    if (
        percent_change >=5 or
        percent_change <=-5
        ):
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
        news_request = requests.get(url=news_url)
        news_data = news_request.json()["articles"][:3]

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASS)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_PASS,
                                 msg=f"Subject:Stock change in {COMPANY_NAME}\n"+
                                    f"""Percentage change: {percent_change}
                                        Article 1:
                                            Title: {news_data[0]["title"]}
                                            Description: {news_data[0]["description"]}
                                        Article 2:
                                            Title: {news_data[1]["title"]}
                                            Description: {news_data[1]["description"]}
                                        Article 3:
                                            Title: {news_data[2]["title"]}
                                            Description: {news_data[2]["description"]}""")
            connection.close()

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

