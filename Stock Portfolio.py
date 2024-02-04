import pandas as pd

class Stock:
    def __init__(initial, symbol, price):
        initial.symbol = symbol
        initial.price = price
        initial.quantity = 0

    def buy(initial, quantity):
        initial.quantity += quantity
        print(f"You have purchased {quantity} shares of {initial.symbol}.")

    def sell(initial, quantity):
        if quantity <= initial.quantity:
            initial.quantity -= quantity
            print(f"You have sold {quantity} shares of {initial.symbol}.")
        else:
            print("You have insufficient shares to sell.")

    def get_value(initial):
        return initial.quantity * initial.price

    def display_info(initial):
        print(f"Stock: {initial.symbol}")
        print(f"Price per share: ${initial.price:.2f}")
        print(f"Quantity: {initial.quantity}")
        print(f"Total Value: ${initial.get_value():.2f}\n")

def generate_stock_portfolio_from_excel(file_path):
    try:
        df = pd.read_excel(file_path)
        portfolio = [Stock(row['Symbol'], row['Price']) for _, row in df.iterrows()]
        return portfolio
    except:
        print("There is an error with the file provided. Please try again :>.")
        return []

def update_stock_prices_in_excel(file_path, portfolio):
    try:
        df = pd.read_excel(file_path)
        for stock in portfolio:
            df.loc[df['Symbol'] == stock.symbol, 'Price'] = stock.price
        df.to_excel(file_path, index=False)
        print("Successfully updated stock prices in the Excel file.")
    except:
        print("There is an error updating the Excel file.")

def display_available_stocks(portfolio):
    print("Available Stocks:")
    for stock in portfolio:
        print(f"{stock.symbol} - Price: ${stock.price:.2f}")

def main():
    file_path = "/Users/athena/Desktop/stock_prices.xlsx"
    stock_portfolio = generate_stock_portfolio_from_excel(file_path)

    display_available_stocks(stock_portfolio)

    cash = 50000

    while True:
        print("\nStock Portfolio Menu:")
        print("1. Display Your Portfolio")
        print("2. Buy Stocks")
        print("3. Sell Stocks")
        print("4. Exit this program")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print(f"Available Cash: ${cash:.2f}")
            for stock in stock_portfolio:
                stock.display_info()
        elif choice == '2':
            symbol = input("Which stock would you like to buy?: ").upper()
            quantity = int(input("How many stocks would you like to buy?: "))
            for stock in stock_portfolio:
                if stock.symbol == symbol:
                    cost = quantity * stock.price
                    if cost <= cash:
                        stock.buy(quantity)
                        cash -= cost
                    else:
                        print("You don't have enough cash for this :<.")
                    break
            else:
                print("You have entered an invalid stock symbol, try again.")
        elif choice == '3':
            symbol = input("Which stock do you want to sell? ").upper()
            quantity = int(input("How many stocks do you want to sell?  "))
            for stock in stock_portfolio:
                if stock.symbol == symbol:
                    stock.sell(quantity)
                    cash += quantity * stock.price
                    break
            else:
                print("You have entered an invalid stock symbol, try again.")
        elif choice == '4':
            update_stock_prices_in_excel(file_path, stock_portfolio)
            print("Exiting this Stock Portfolio. BYEEEEEEEEEE!")
            break
        else:
            print("Choice Invalid :< , please enter a number between 1 and 4 :)")

if __name__ == "__main__":
    main()
