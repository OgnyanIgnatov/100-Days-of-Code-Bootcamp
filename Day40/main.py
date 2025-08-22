#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from datetime import datetime, timedelta
from notification_manager import send_message


today = datetime.now()
tomorrow = today + timedelta(1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

ORIGIN_IATA = "LON"

data_manager = DataManager()
sheet_data = data_manager.get_destination_prices_data()['prices']
users_data = data_manager.get_customer_emails()
flight_search = FlightSearch()

for el in sheet_data:
        flight_search_response = flight_search.process(el["city"])
        el["iataCode"] = flight_search_response

print(sheet_data)
data_manager.data = sheet_data
data_manager.update_iata_codes()

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    
    flights = flight_search.check_flights(
        ORIGIN_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today,
        is_direct=True
    )

    if flights is not None: 
        cheapest_flight_data = find_cheapest_flight(flights)
    else:
        flights = flight_search.check_flights(
            ORIGIN_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today,
            is_direct=False,
        )
    
    if flights is not None:
        cheapest_flight_data = find_cheapest_flight(flights)
    
    if cheapest_flight_data is not None:
        cheapest_flight = float(cheapest_flight_data.price)
        if cheapest_flight <= destination['lowestPrice']:
                send_message(users_data, cheapest_flight, ORIGIN_IATA, destination['iataCode'], cheapest_flight_data.out_date, cheapest_flight_data.return_date)
    
