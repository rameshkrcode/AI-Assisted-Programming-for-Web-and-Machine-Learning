
import requests
import time
import datetime

def scrape_crypto_prices(crypto_id="bitcoin"):
    """ Fetch cryptocurrency price data and log trends """
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd"
    while True:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            price = data[crypto_id]["usd"]
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{timestamp}] {crypto_id.capitalize()} Price: ${price}")
        else:
            print(f"Error fetching data: {response.status_code}")
        time.sleep(3600)  # Fetch every hour

# Example usage
scrape_crypto_prices("ethereum")
