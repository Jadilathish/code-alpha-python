import requests
import json

API_KEY = "YOUR_ALPHAVANTAGE_API_KEY"
BASE_URL = "https://www.alphavantage.co/query"

portfolio = {}

def get_stock_price(symbol):
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": "5min",
        "apikey": API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    try:
        latest_time = list(data["Time Series (5min)"].keys())[0]
        return float(data["Time Series (5min)"][latest_time]["1. open"])
    except KeyError:
        print("Error retrieving stock data. Check API key or stock symbol.")
        return None

def add_stock(symbol, quantity):
    price = get_stock_price(symbol)
    if price:
        portfolio[symbol] = {"quantity": quantity, "price": price}
        print(f"Added {quantity} shares of {symbol} at ${price:.2f} each.")

def remove_stock(symbol):
    if symbol in portfolio:
        del portfolio[symbol]
        print(f"Removed {symbol} from portfolio.")
    else:
        print("Stock not found in portfolio.")

def view_portfolio():
    print("\nStock Portfolio:")
    total_value = 0
    for symbol, details in portfolio.items():
        stock_value = details["quantity"] * details["price"]
        total_value += stock_value
        print(f"{symbol}: {details['quantity']} shares @ ${details['price']:.2f} each (Total: ${stock_value:.2f})")
    print(f"Total Portfolio Value: ${total_value:.2f}\n")

def main():
    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        if choice == "1":
            symbol = input("Enter stock symbol: ").upper()
            quantity = int(input("Enter quantity: "))
            add_stock(symbol, quantity)
        elif choice == "2":
            symbol = input("Enter stock symbol to remove: ").upper()
            remove_stock(symbol)
        elif choice == "3":
            view_portfolio()
        elif choice == "4":
            print("Exiting Portfolio Tracker.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
