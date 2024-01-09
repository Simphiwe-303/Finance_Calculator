import math
import sys

print("Investment - calculates the amount of interest you'll earn on your investment.")
print("Bond - calculates the amount you'll have to pay on a home loan.\n")

usr_inpt = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

# If the user input is investment the following if statement will run
if usr_inpt == "investment":
        amount = input("How much are you depositing: ")
        int_rate = input("The interest rate:")
        num_years = input("The number of months you are planning on investing is: ")
        interest = input("What kind of interest would you like(Simple/Compound): ").lower()

        # Calculates the Simple interest amount that the user will get after a certain number of months or years
        if interest == "simple":
                P = int(amount)
                r = int(int_rate) / 100
                t = int(num_years)

                A = P * (1 + r * t)
                print("The simple interest amount that you will get after " + str(t) + " month/s is R" + str(A))

        # Calculates the Compound interest amount that the user will get after a certain number of months or years
        elif interest == "compound":
                P = int(amount)
                r = int(int_rate) / 100
                t = int(num_years)

                A = P * math.pow((1 + r), t)
                print("The simple compount interest amount that you will get after " + str(t) + " month/s is R" + str(A))

        # If the user enter anything either than Simple or Compound the else statement will be executed
        else:
                print("Follow the instruction and you'll be fine")
                sys.exit()

# if the user input bond the following elif statement will run
elif usr_inpt == "bond":
        house = input("Please enter the present value of the house: ")
        int_rate = input("The interest rate is: ")
        months = input("The number of months you plan to take to repay the bond is: ")

        # Bond repayment calculations

        P = int(house)
        i = (int(int_rate) / 100) / 12
        n = int(months) 

        repayment = i * P / (1 - (1 + i) ** (-n))
        print("You will have to pay R" + str(repayment) + " each month.")

# If the user enter anything either than investement or bond the following is executed
else:
        print("Read carefully")
        sys.exit()
