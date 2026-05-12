# A customer visits a supermarket and buys several items. Write a program that:
# Stores the item names and their prices in two separate lists.
# Calculates the total bill amount.
# Applies a discount based on the total:
# If total > ₹1000 → 20% discount
# If total > ₹500 → 10% discount
# Otherwise → no discount
# Checks if the customer is a member — members get an extra 5% off on the final amount.
# Prints an itemized bill and the final amount payable.
print("____This is a supermarket____")
print("These are the list of items")
item_name=['Battery','Soap','Utensils']
print("These are the prices for each items")
item_price=[50,500,1200]
total_price=item_price[0]+item_price[1]+item_price[2]
if total_price > 1000:
    total_price=total_price-total_price*20/100
    print(f"Congrats! You got 20% discount and your total price after discount is: {total_price}")
elif total_price > 500:
    total_price=total_price-total_price*10/100
    print(f"Congrats! You got 10% discount and your total price after discount is: {total_price}")
else:
    print(f"Your total price is: {total_price}")

customer="members"
if customer=="members":
    total_price=total_price-(total_price*5/100)
    print(f"Congrats! You got 15% discount because you wre a member and spent more than 1000 {total_price}")

print("___SuperMarket Bill___")
print(f"{item_name[0]} : {item_price[0]}")
print(f"{item_name[1]} : {item_price[1]}")
print(f"{item_name[2]} : {item_price[2]}")
print("___Net Price___")
print(f"The total price is {total_price}")