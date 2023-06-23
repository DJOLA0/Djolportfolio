import math
# define your functions for calculations based on user inputs
print("choose Flights to London, Paris or New York")
def hotel_cost(x, num_nights):
    stay_price = x * num_nights
    return stay_price

def plane_cost(city_flight):
    return city_flight * 2

def car_rental(rental,x):
    rental_days = x * 50
    return rental_days

# use this to call user inputs
def gettin_user_input(question):
    user_input = input(question)
    return user_input

# define a function for the total 
def holiday_cost(x=0, y=0, z=0):
    total = x + y + z
    return total
# prompt the user to choose from any of the destinations
print("London, Paris, New York")

city = gettin_user_input("where are you flying to?: ").lower()
num_nights = gettin_user_input("How many nights are you going?: ")
rental_days = gettin_user_input("how many days do you need a car?: ")
print("You have chosen: " + city)
# call the functons to calculate individual costs for each city and get the total
if city == str("london"):
    num1 = hotel_cost(400, int(num_nights))
    num2 = plane_cost(187)
    num3 = car_rental(int(rental_days), 50)
    total = holiday_cost(num1 + num2 + num3)
    print("Total cost for this trip: £",total)
elif city == str("paris"):
    num1 = hotel_cost (1500, int(num_nights))
    num2 = plane_cost(200)
    num3 = car_rental(int(rental_days), 50)
    total = holiday_cost(num1 + num2 + num3)
    print("Total cost for this trip: £",total)
elif city == str("new york"):
    num1 = hotel_cost (4000, int(num_nights))
    num2 = plane_cost(620)
    num3 = car_rental(int(rental_days), 50)
    total = holiday_cost(num1 + num2 + num3)
    print("Total cost for this trip: £",total)
# prevent the code crashing by invalid input
else: 
    print("not available")