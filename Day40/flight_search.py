import os, requests
from dotenv import load_dotenv



AMADEUS_TOKEN_ENDPOINT = os.getenv("AMADEUS_TOKEN_ENDPOINT")
IATA_ENDPOINT = os.getenv("IATA_ENDPOINT")
AMADEUS_SEARCH_ENDPOINT = os.getenv("AMADEUS_ENDPOINT") + "/shopping/flight-offers"



load_dotenv()
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def _get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': os.getenv("AMADEUS_API_KEY"),
            'client_secret': os.getenv("AMADEUS_API_SECRET"),
        }
        request = requests.post(url=AMADEUS_TOKEN_ENDPOINT, headers=header, data=body)

        return request.json()["access_token"]
    
    def __init__(self):
        self._api_key = os.getenv("AMADEUS_API_KEY")
        self._api_secret=os.getenv("AMADEUS_API_SECRET")
        self._token = self._get_new_token()
    
    def process(self,city):
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "keyword": city,
            "max": "2",
            "include": "AIRPORTS",
        }
        response = requests.get(url=IATA_ENDPOINT, headers=headers, params=query)

        code = response.json()["data"][0]['iataCode']
        return code
    
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time, is_direct = True):
        header = {
            "Authorization": f"Bearer {self._token}"
        }
        params = {
                "originLocationCode" : origin_city_code,
                "destinationLocationCode" : destination_city_code,
                "departureDate" : from_time.strftime("%Y-%m-%d"),
                "returnDate": to_time.strftime("%Y-%m-%d"),
                "adults": 1,
                "nonStop": is_direct,
                "currencyCode": "GBP",
                "max": "10",
            }
        response = requests.get(url=AMADEUS_SEARCH_ENDPOINT, headers=header, params=params)

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("Response body:", response.text)
            return None
        
        return response.json()
        