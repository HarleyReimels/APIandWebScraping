import DailyAPI

# Calls function to get weather
weather = DailyAPI.get_weather("Saluda, SC", "US", "29037")

# Prints weather
for item in weather:
    print(item)
    
