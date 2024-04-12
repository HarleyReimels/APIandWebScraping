import requests
import constants
# Information provided at
# https://rapidapi.com/weatherapi/api/weatherapi-com/

def get_weather(town, country, zip):
    # Connect to website to get Json
    url = "https://weatherapi-com.p.rapidapi.com/current.json"

    # Really Ugly way to safely load keys, need to investigate a better method
    rapid_Api_Key_1 = constants.rapid_Api_Key_1
    rapid_Api_Key_2 = constants.rapid_Api_Key_2
    rapid_Api_Host_1 = constants.rapid_Api_Host_1
    rapid_Api_Host_2 = constants.rapid_Api_Host_2
    
    # Location
    querystring = {"q":f"{town} {country} {zip}"}

    headers = {
        rapid_Api_Key_1: rapid_Api_Key_2,
        rapid_Api_Host_1: rapid_Api_Host_2
    }

    # Loads information into response variable
    response = requests.get(url, headers=headers, params=querystring)
    location = []
    current = []
    
    # Prints information of location
    for k, v in response.json()["location"].items():
        location.append(f"{k.capitalize()}: {v}")

    # Prints information of current
    for k, v in response.json()["current"].items():
        current.append(f"{k.capitalize()}: {v}")
        
    # Combine both lists
    weather = location + current
    
    return weather
