import requests
import os
from dotenv import load_dotenv

load_dotenv()
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")


class DataManager:
      def __init__(self):
           self.data = {}

      def get_destination_data(self):
            response = requests.get(url=SHEETY_ENDPOINT)
            self.data = response.json()
            return self.data

      def update_iata_codes(self):
            
            for el in self.data:
                  iata_change = {
                        'price' :{
                              'iataCode' : el['iataCode']
                        }
                  }
                  request = requests.put(url=SHEETY_ENDPOINT + f"/{el['id']}", json=iata_change)
                  print(request.text)
      


