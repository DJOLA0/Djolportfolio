# list to be iterated through
mine_sweep = [['-', '#', '-', '#', '-'], 
             ['-', '#', '-', '#', '-'],
             ['-', '#', '-', '#', '-'],
             ['-', '#', '-', '#', '-'],
              ]  
# make the number of columns depend on length of row
for i in range(len(mine_sweep)):
    if mine_sweep[i] == '-':
        mine_sweep[i] = 0
    elif mine_sweep[i] == '#':
        mine_sweep[i] = 2
print(mine_sweep)


def hotel_cost(x):
    result = x * 2
    print("Inside function: " + str(result)) 
x = 3
double(x)
result = x * 2
print("Outside function: " + str(result))

# code that takes number of nights as input and returns total cost of hotel
# I decide 140 a night is the base rate for all hotel stays to not ove complicate things
# print calculation based on user input
def hotel(num_nights):
    hotel_cost = 140 * num_nights
    return hotel_cost

def hotel(num_nights):
    if num_nights == int(input("How many days are you staying in the hotel? :")):
        hotel_cost = 140 * num_nights
    return(f"you are staying for {num_nights} day, which will cost {hotel_cost}")

# define the function for car rental
def rental(rental_days):
    car_rental = 50 * rental_days
    return car_rental

def rental(rental_days):
    if rental_days == int(input("How many days are you need a car? :")):
        car_rental = 50 * rental_days
    return(f"you are renting for {rental_days} day, which will cost {car_rental}")