#  Real Estate Screener
# You're building a property screener. A user types in a property's price in lakhs. Your program should:

# Take the price as input from the user
# Store it as a float (not int, not string) — because property prices can be like 85.5 lakhs
# Create a boolean variable is_affordable that is True if the price is at or below 150.0, otherwise False
# Print is_affordable

# Write the 3-line program.
price=float(input("Enter the price of the real state: "))
is_affordable=price <= 150.0
print(bool(is_affordable))
