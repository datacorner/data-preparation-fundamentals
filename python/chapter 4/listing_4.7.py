import pandas as pd
import requests
# It may be necessary to install via pip the library BeautifulSoup4
from bs4 import BeautifulSoup

# BE CAREFUL !
# This code worked on january 2025 but not not anymore if the website changed the structure of the HTML page requested.

if __name__ == "__main__":
    url = "https://store.steampowered.com/app/2358720/Black_Myth_Wukong/"
    response = requests.get(url) 
    if response.status_code == 200: 
        soup = BeautifulSoup(response.content, 'html.parser') 
        price_div = soup.find("div", class_="game_purchase_price") 
        if price_div:
            price = price_div.text.strip()
            print(f"Latest Price: {price}")
        else:
            print("Price information not found on the page.")
    else:
        print("Failed to retrieve the page")
