full_name = input("what is your full name? ")

if len(full_name) >= 4:
    print("Thank you for entering your name")

elif len(full_name) > 25:
    print("You have entered more than 25 characters. Please make sure that you have only entered your full name.")
    
elif len(full_name) < 4:
    print ("you have entered less than 4 characters. Please make sure that you have only entered your full name.")

else: 
    print("you haven't entered anything. Please enter your full name.")