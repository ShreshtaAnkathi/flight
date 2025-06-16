# import csv 
# import requests

# CLIENT_ID = "AJufiYsfUSLyRDltUhHlTasCl8n1glj8"
# CLIENT_SECRET = "Cq1JF4M4HRGEeN0I"

# airline_map = {
#     "6E": "IndiGo",
#     "AI": "Air India",
#     "SG": "SpiceJet",
#     "UK": "Vistara",
#     "G8": "GoAir",
#     "I5": "AirAsia India",
    
# }

# def get_access_token():
#     url = "https://test.api.amadeus.com/v1/security/oauth2/token"
#     data = {
#         "grant_type": "client_credentials",
#         "client_id": CLIENT_ID,
#         "client_secret": CLIENT_SECRET
#     }
#     response = requests.post(url, data=data)
#     return response.json().get("access_token")

# def get_airline_name(carrier_code):
#     return airline_map.get(carrier_code, carrier_code)  

# def search_flights(from_code, to_code, date):
#     token = get_access_token()
#     headers = {
#         "Authorization": f"Bearer {token}"
#     }
#     params = {
#         "originLocationCode": from_code,
#         "destinationLocationCode": to_code,
#         "departureDate": date,
#         "adults": 1,
#         "currencyCode": "INR",
#         "max": 5
#     }

#     url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
#     res = requests.get(url, headers=headers, params=params)

#     if res.status_code == 200:
#         data = res.json()["data"]
#         for flight in data:
#             price = flight["price"]["total"]

           
#             print(f"Price: ₹{price}")
#           #  print("Segments:")
#             for segment in flight["itineraries"][0]["segments"]:
#                 carrier_code = segment["carrierCode"]
#                 flight_number = segment["number"]
#                 airline_name = get_airline_name(carrier_code)
#                 departure = segment["departure"]["at"]
#                 arrival = segment["arrival"]["at"]

#                 flight_name = f"{airline_name} {flight_number}"
#                 print(f"  Flight: {flight_name}")
#                 print(f"  Departure: {departure}")
#                 print(f"  Arrival: {arrival}")
#                 print("-" * 20)
#             print("=" * 40)
#     else:
#         print("Error:", res.json())

# from_city = input("From (e.g., HYD): ")
# to_city = input("To (e.g., DEL): ")
# date = input("Date (YYYY-MM-DD): ")
# search_flights(from_city, to_city, date)




#import csv
import requests

CLIENT_ID = "AJufiYsfUSLyRDltUhHlTasCl8n1glj8"
CLIENT_SECRET = "Cq1JF4M4HRGEeN0I"

airline_map = {
    "6E": "IndiGo",
    "AI": "Air India",
    "SG": "SpiceJet",
    "UK": "Vistara",
    "G8": "GoAir",
    "I5": "AirAsia India",
    "QR": "Qatar Airways",
    "EK": "Emirates",
    "LH": "Lufthansa",
    "LO": "LOT Polish Airlines",
    "TK": "Turkish Airlines",
    "LX": "Swiss International Air Lines",
    "DE": "Condor",
   
}

def get_access_token():
    url = "https://test.api.amadeus.com/v1/security/oauth2/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }
    response = requests.post(url, data=data)
    return response.json().get("access_token")

def get_airline_name(carrier_code):
    return airline_map.get(carrier_code, carrier_code)

def search_flights(from_code, to_code, date):
    token = get_access_token()
    headers = {
        "Authorization": f"Bearer {token}"
    }
    params = {
        "originLocationCode": from_code,
        "destinationLocationCode": to_code,
        "departureDate": date,
        "adults": 1,
        "currencyCode": "INR",
        #"max": 25
    }

    url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
    res = requests.get(url, headers=headers, params=params)

    if res.status_code == 200:
        data = res.json()["data"]
        csv_data = []

        for flight in data:
            price = flight["price"]["total"]
            print(f"Price: ₹{price}")

            for segment in flight["itineraries"][0]["segments"]:
                carrier_code = segment["carrierCode"]
                flight_number = segment["number"]
                airline_name = get_airline_name(carrier_code)
                departure = segment["departure"]["at"]
                arrival = segment["arrival"]["at"]

                flight_name = f"{airline_name} {flight_number}"
                print(f"  Flight: {flight_name}")
                print(f"  Departure: {departure}")
                print(f"  Arrival: {arrival}")
                print("-" * 20)

               
        #         csv_data.append({
        #             "Flight": flight_name,
        #             "Departure": departure,
        #             "Arrival": arrival,
        #             "Price (INR)": price
        #         })

        #     #hprint("=" * 40)

      
        # with open("flights1.csv", "w", newline="", encoding="utf-8") as csvfile:
        #     fieldnames = ["Flight", "Departure", "Arrival", "Price (INR)"]
        #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #     writer.writeheader()
        #     writer.writerows(csv_data)

        # print("✅ Flight data exported to 'flights1.csv'")

    else:
        print("❌ Error:", res.json())


from_city = input("From (e.g., HYD): ")
to_city = input("To (e.g., DEL): ")
date = input("Date (YYYY-MM-DD): ")
search_flights(from_city, to_city, date)
