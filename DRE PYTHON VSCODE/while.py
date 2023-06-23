# starting number initialize 0 for nice range
# count for the sequence of inputs
total = 0
average = 0
count = 0

user_input = int(input("enter a number (-1 to exit)"))

# loop for the repeating number inputs
while user_input != -1 :
    total += user_input
    count += 1
# how to calculate mean average
    average = total / count
    user_input = int(input("enter a number (-1 to exit)"))

# outputs for when the loop is to be stopped    
    if user_input == -1:
        print("total:", total)
        print("The average:, ", average) 
        break


    
