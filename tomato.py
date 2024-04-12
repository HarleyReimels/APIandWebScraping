# Tomato soup

def soup_quotes():
    import requests
    from bs4 import BeautifulSoup

    # Store html file
    index = requests.get("https://quotes.toscrape.com/")

    # Write html to txt document
    with open("file.txt", "w", encoding="utf=8") as file:
        file.write(index.text)

    # Use Beautiful Soup to make it parseable
    with open('file.txt', encoding="utf=8") as fp:
        soup = BeautifulSoup(fp, features="html.parser")

    # Use findall to retrieve all quotes and authors
    my_quote = soup.find_all('span', class_ = "text")
    my_author = soup.find_all('small', class_= "author")
    finished_quote = []
    finished_author = []

    # Remove Smart Quotes and get text from tag
    for item in my_quote:
        finished_quote.append(item.get_text().replace('\u201c', '').replace('\u201d', ''))
    # Get Author from tag
    for item in my_author:
        finished_author.append(item.get_text())
        
    # Zip the authors with their quotes
    quote_and_author = zip(finished_quote, finished_author)

    return quote_and_author

        
    #TODO: There are many more quotes on many more pages. Need to implement Selenium to browse pages to retrieve more quotes.