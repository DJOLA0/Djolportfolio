import math

#  instruction for output choice
print("investment   - to calculate the amount of interest you'll earn on your investment")
print("bond   - to calculate the amount you'll have to pay on a home loan")

# users sees output and chooses method
question = input("Enter either 'investment' or 'bond' from the menu to proceed: ").lower()
print(question)

if question == "bond": # alternatively, if the user goes with the 'bond' option
    print("you have chosen bond")
    home_value = int(input("how much is your house? (£): "))
    interest_rate = float(input("Enter your interest rate (%): "))
    months = int(input("how many months are you repaying for? "))
    monthly_interest_rate = (interest_rate / 100) / 12 # calculation for the users inputs and print the monthly repayment cost
    repayment = (monthly_interest_rate * home_value) / (1 - math.pow (1 + monthly_interest_rate, - months))
    print(f"£{round(repayment,2)} a month")

# how much money they want to deposit
# if the user wants to look at the invest option
elif question == "investment":
    print("you have chosen investment.")
    deposit_amount = int(input("How much are you depositing? (£): ")) 
    interest_rate = float(input("Enter your interest rate (%): "))
    years_invested = int(input("How many years are you investing?: "))
    while True: # try-except block to handle valueError if user enters the wrong thing
            try:
                interest_type = input("enter 'simple' or 'compound': ").lower()
                if interest_type == "simple" or interest_type == "compound":
                    if interest_type == "simple": # calculation for simple
                        simple_amount = deposit_amount + (deposit_amount * (interest_rate / 100) * years_invested)
                        print(f"The simple interest earned is: £{simple_amount}")
                    if interest_type == "compound": # calculation for compound
                        compound_amount = deposit_amount * math.pow ((1 + (interest_rate / 100)) , years_invested)# math.pow 
                        print(f"The compound interest earned is: £{round(compound_amount,2)}")  
                    break
                else:
                    print("Invalid input")
            except ValueError:
                print("Invalid input. Please enter 'simple' or 'compound'")
            

