
# Retrieves quotes from website when ran directly
if __name__ == "__main__":
    import requests

    url = "https://zenquotes.io/api/quotes/"
    quote = requests.get(url)
