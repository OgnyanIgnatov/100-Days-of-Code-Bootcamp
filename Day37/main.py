import requests
from datetime import datetime, timedelta

USERNAME = "...."
TOKEN = "...."
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint =  pixela_endpoint + f"/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN" : TOKEN
}

graph_params = {
    "id" : GRAPH_ID,
    "name" : "Drinking Graph",
    "unit" : "liter",
    "type" : "int",
    "color" : "sora",
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers )
# print(response.text)
# 
pixel_post_endpoint = pixela_endpoint + f"/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_post_params = {
    "date" : today.strftime("%Y%m%d"), 
    "quantity" : input("How many liters of rakia did you drink today?: "),
}

# response = requests.post(url=pixel_post_endpoint, json=pixel_post_params, headers=headers)
# print(response.text)

update_post_endpoint = pixela_endpoint + f"/{USERNAME}/graphs/{GRAPH_ID}/{(today - timedelta(days=1)).strftime("%Y%m%d")}"
update_post_params = {
    "quantity" : "2",
}

# response = requests.put(url=update_post_endpoint, json=update_post_params, headers=headers)
# print(response.text)

delete_post_endpoint = update_post_endpoint

# response = requests.delete(url=delete_post_endpoint,headers=headers)
# print(response.text)