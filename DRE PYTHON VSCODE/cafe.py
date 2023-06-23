import math

# create menu list
int_menu_list = {1: "Tea", 
                 2: "Biscuits", 
                 3: "coffee", 
                 4: "muffins" 
                 }
# create a new dictionary with stock
stock = {'Tea' : 10, 
              'Biscuits' : 22, 
              'coffee' : 30, 
              'muffins' : 17
              }
# create a dictionary with the price
price = {'Tea': 2.30, 
              'Biscuits' : 1.50, 
              'coffee' : 3, 
              'muffins' : 1.50
              }
# initialise the stock variable
total_stock =0
# create a for loop to loop through each item
# retrieve the price and the stock
for item in price:
    value = price[item] * stock[item]
    total_stock += value
# print the total using an f string
print(f"Total Stock: £{total_stock:.2f}")