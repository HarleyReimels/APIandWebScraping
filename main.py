import DailyAPI
import json
import tomato


################# Weather API Call Section #######################
######### https://rapidapi.com/weatherapi/api/weatherapi-com/ ####

# Calls function to get weather
weather = DailyAPI.get_weather("Saluda, SC", "US", "29037")

# Prints weather
for item in weather:
    print(item)


################# Quote API Call Section #######################
########### https://zenquotes.io/api/quotes/ ###################

# Opens and loads Json
with open('test.json') as f:
    content = json.load(f)

# Assigns all items under All to my_q
my_q = content["all"]

# Prints all quotes and authors
for item in my_q:
    print(f"{item['q']} {item['a']}")


################# Beautiful Soup Scraping Section #######################
################## https://quotes.toscrape.com/ #########################
# Print Beautiful Soup quotes and authors
my_soup = tomato.soup_quotes()
for item in my_soup:
    print("\n", item[0], item[1])
