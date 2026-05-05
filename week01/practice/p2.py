# WAP to take a stock name, today's price and yesterday's price from the user,
# check if the price went up or down using bool, and display the result.

stock_name = input("Enter the name of the stock: ")
yesterday_price = float(input("Enter the price of this stock yesterday: "))
today_price = float(input("Enter the price of this stock today: "))

price_went_up = today_price > yesterday_price

if price_went_up:
    print(f"The price of {stock_name} has increased")
elif today_price==yesterday_price :
    print(f"The price of {stock_name} has not changed")
else:
    print(f"The price of {stock_name} has decreased")


    