import requests
import os
from dotenv import load_dotenv

load_dotenv()


class DataManager:
      def __init__(self):
            self.prices_data = {}
            self.users_data = []
            self.SHEETY_PRICES_ENDPOINT = os.getenv("SHEETY_PRICES_ENDPOINT")
            self.SHEETY_USERS_ENDPOINT = os.getenv("SHEETY_USERS_ENDPOINT")

      def get_destination_prices_data(self):
            response = requests.get(url=self.SHEETY_PRICES_ENDPOINT)
            self.prices_data = response.json()
            return self.prices_data

      def update_iata_codes(self):
            
            for el in self.prices_data:
                  iata_change = {
                        'price' :{
                              'iataCode' : el['iataCode']
                        }
                  }
                  request = requests.put(url=self.SHEETY_PRICES_ENDPOINT + f"/{el['id']}", json=iata_change)
                  print(request.text)
      
      def get_customer_emails(self):
            response = requests.get(url=self.SHEETY_USERS_ENDPOINT)
            data = response.json()["users"]
            for el in data:
                  self.users_data.append(el["What's your email?"])
            return self.users_data
            
      


