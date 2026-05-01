# WAP to take a stock name, today's price and yesterday's price from the user,
# check if the price went up or down using bool, and display the result.

stock_name = input("Enter the name of the stock: ")
yesterday_stock_price = float(input("Enter the price of the stock: "))
today_stock_price = float (input("Enter the price of the stock today: "))
price_stock= yesterday_stock_price < today_stock_price

# f string
print("_________")
print(f"Stock: {stock_name}")
print(f"Today: {today_stock_price}")
print(f"Yesterday: {yesterday_stock_price}")

print(price_stock)