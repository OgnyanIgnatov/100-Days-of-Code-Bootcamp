import requests, smtplib, time
from datetime import datetime


parameters = {
    "lat":42.697333,
    "lng":23.322001,
    "formatted":0
}

def is_iss_over():
    request=requests.get(url="http://api.open-notify.org/iss-now.json")
    request.raise_for_status()
    data = request.json()

    longitude = float(data['iss_position']['longitude'])
    latitude = float(data['iss_position']['latitude'])

    diff_lng = longitude - parameters['lng']
    diff_lat = latitude - parameters['lat']

    if -5<=diff_lng<=5 and -5<=diff_lat<=5:
        return True
    
    return False


def is_night():
    response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
    sunset = data['results']['sunset'].split('T')[1].split(':')[0]

    time_now = datetime.now().hour

    if time_now >= sunset or time_now<=sunset:
        return True
    
    return False


my_email = ":)"
my_password = ":P"

while True:
    time.sleep(60)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email,my_password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg="Look up!")
