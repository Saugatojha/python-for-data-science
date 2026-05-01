stock_price= 233.32  #vairables in py integer, float, string, bool
stock_name= 'HRL'
stock_number=1

stock_price_2=232.31;stock_name_2='HBL' # like c/cpp we can use ; the use of semicolon is to mark end of the line and let the code goto next line here 2 codes are in 1 line ; sperates this

print(stock_price)
print(stock_name)
print(stock_number)
print(stock_price_2)
print(stock_name_2)

price_increase = True
price_decrease = False
print("___Boolean___")
print(int(price_increase)) # 1
print(int(price_decrease)) # 0

print(bool(0)) # False
print(bool(1)) # True


print ("These all act like False:")
print(bool(0))      # False
print(bool(0.0))    # False
print(bool(""))     # False
print(bool([]))     # False
print(bool(None))   # False

print("These all act as True")
print(bool(100))       # True
print(bool(3.14))      # True
print(bool("NEPSE"))   # True
print(bool([1,2,3]))   # True