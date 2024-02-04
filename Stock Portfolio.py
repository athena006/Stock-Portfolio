import pandas as pd

class Stock:
  def __init__(self, symbol, price):
    self.symbol = symbol
    self.price = price
    self.quantity = 0

  def buy(self, quantity):
    self.quantity += quantity
    print(f"You have purchased {quantity} shares of {self.symbol}.")

  def sell(self, quantity):
    if quantity <= self.quantity:
      self.quantity -= quantity
      print(f"You have sold {quantity} shares of {self.symbol}.")
    else:
      print("Insufficient shares to sell.")
      
  def get_value(self):
    return self.quantity * self.price

  def display_info(self):
    print(f"Stock: {self.symbol}")
    print(f"Price per share: ${self.price:.2f}")
    print(f"Quantity: {self.quantity}")
    print(f"Total Value: ${self.get_value():.2f}\n")

def generate_stock_portfolio_from_excel(file_path):
  try:
    df = pd.read_excel(file_path)
    portfolio = [Stock(row['Symbol'], row['Price']) for _, row in df.iterrows()]
    return portfolio
  except Exception as e:
    print(f"Error reading Excel file: {e}")
    return []

def update_stock_prices_in_excel(file_path, portfolio):
  try:
    df = pd.read_excel(file_path)
    for stock in portfolio:
      df.loc[df['Symbol'] == stock.symbol, 'Price'] = stock.price
      df.to_excel(file_path, index=False)
      print("Updated stock prices in the Excel file.")
  except Exception as e:
    print(f"Error updating Excel file: {e}")

def display_available_stocks(portfolio):
  print("Available Stocks:")
  for stock in portfolio:
    print(f"{stock.symbol} - Price: ${stock.price:.2f}")

def main():
  file_path = "/Users/athena/Desktop/stock_prices.xlsx"
  stock_portfolio = generate_stock_portfolio_from_excel(file_path)

  display_available_stocks(stock_portfolio)

  cash = 5000  # Starting cash amount

  while True:
    print("\nStock Portfolio Menu:")
    print("1. Display Portfolio")
    print("2. Buy Stock")
    print("3. Sell Stock")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
      print(f"Available Cash: ${cash:.2f}")
      for stock in stock_portfolio:
        stock.display_info()
    elif choice == '2':
      symbol = input("Enter the stock symbol you want to buy: ").upper()
      quantity = int(input("Enter the quantity you want to buy: "))
      for stock in stock_portfolio:
        if stock.symbol == symbol:
          cost = quantity * stock.price
        if cost <= cash:
          stock.buy(quantity)
          cash -= cost
        else:
          print("Not enough cash to buy.")
           break
      else:
        print("The entered stock symbol is invalid.")
    elif choice == '3':
        symbol = input("Enter the stock symbol you want to sell: ").upper()
        quantity = int(input("Enter the quantity you want to sell: "))
      for stock in stock_portfolio:
        if stock.symbol == symbol:
           stock.sell(quantity)
           cash += quantity * stock.price
           break
        else:
          print("The entered stock symbol is invalid.")
    elif choice == '4':
      update_stock_prices_in_excel(file_path, stock_portfolio)
      print("Exiting Stock Portfolio. Farewell!")
      break
else:
  print("Enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
