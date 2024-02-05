import pandas as pd

class Stock:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price
        self.quantity = 0

    def buy(self, quantity):
        self.quantity += quantity
        print(f"You have purchased {quantity} shares of {self.symbol} at {self.price} each.")

    def sell(self, quantity):
        if quantity <= self.quantity:
            self.quantity -= quantity
            print(f"You have sold {quantity} shares of {self.symbol} at {self.price} each.")
        else:
            print("You do not have enough shares to sell. :<")

    def get_value(self):
        return self.price * self.quantity

    def display(self):
        print(f"Stock: {self.symbol}")
        print(f"Price per share: ${self.price:.2f}")
        print(f"Quantity: {self.quantity}")
        print(f"Total Value: ${self.get_value():.2f}\n")

def generate_portfolio(file_path):
    try:
        df = pd.read_excel(file_path)
        portfolio = [Stock(row['Symbol'], row['Price']) for _, row in df.iterrows()]
        return portfolio  # Added return statement
    except:
        print("There is an error in the file linked. Please try again or modify the file path :>")
        return []

def update_portfolio(file_path, portfolio):
    try:
        df = pd.read_excel(file_path)
        for stock in portfolio:
            df.loc[df['Symbol'] == stock.symbol, 'Price'] = stock.price
        df.to_excel(file_path, index=False)
        print("Successfully updated stock prices in the Excel file.")
    except:
        print("There is an error updating the Excel file. Try again or modify the file path :>")

def display_stocks(portfolio):
    print("Available Stocks:")
    for stock in portfolio:
        print(f"Stock: {stock.symbol} - Price: ${stock.price:.2f}")

def main():
    file_path = "/Users/athena/Desktop/stock_prices.xlsx"
    portfolio = generate_portfolio(file_path)

    display_stocks(portfolio)

    cash = 50000

    while True:
        print("\nStock Portfolio Menu:")
        print("Press 1 to display your portfolio")
        print("Press 2 to buy stocks")
        print("Press 3 to sell stocks")
        print("Press 4 to exit this program")

        choice = input("Press the numbers on your keyboard to select your choice: ")

        if choice == '1':
            total_portfolio_value = sum(stock.get_value() for stock in portfolio)
            print(f"You have ${cash:.2f} in cash.")
            print(f"The value of your portfolio is ${total_portfolio_value:.2f}")

            for stock in portfolio:
                stock.display()

        elif choice == '2':
            symbol = input("Which stock would you like to buy?: ").upper()
            quantity = int(input("How many stocks would you like to buy?: "))
            for stock in portfolio:
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
            for stock in portfolio:
                if stock.symbol == symbol:
                    stock.sell(quantity)
                    cash += quantity * stock.price
                    break
            else:
                print("You have entered an invalid stock symbol, try again.")

        elif choice == '4':
            update_portfolio(file_path, portfolio)
            print("Exiting this stock portfolio. BYEEEEEEEEEE!")
            break

        else:
            print("Choice Invalid :< , please enter a number between 1 and 4 :)")

if __name__ == "__main__":
    main()
