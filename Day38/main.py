import requests, os
from datetime import datetime
from requests_oauthlib import OAuth1

APP_ID = "..."
API_KEY = "..."
GENDER = "male"
WEIGHT_KG = 90
HEIGHT_CM = 180
AGE = 20

headers = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY,
}

auth_header = {
    "Authorization" : "..."
}

exercise_text = input("Tell me which exercises you did: ")

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

site_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
result = requests.post(url=site_endpoint, json=parameters, headers=headers).json()

sheet_endpoint = "..."

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=auth_header)

    print(sheet_response.text)

