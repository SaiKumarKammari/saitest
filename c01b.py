print("""
This Find Interest application will ask user to specify the amount 

of a principal, an interest rate, and the number of years.

The application calculates and displays the simple interest 

for the given amount at the specified interest for a specified number 

of years.
""")

loan_amount = int(input("Enter the amount of loan (e.g. 1500 for $1,500): "))
interest_rate = float(input("Enter the annual interest rate (e.g. 3.25 for 3.25%): "))
years = int(input("Enter the number of years (e.g. 3 for 3 years): "))

simple_interest = loan_amount * (interest_rate / 100) * years

print(f"\nThe simple interest on a loan of ${loan_amount} at {interest_rate}%  yearly interest rate for {years} years is ${simple_interest:.2f}.")

n = 12
compounded_amount = loan_amount * (1 + (interest_rate / 100) / n) ** (n * years)

print(f"The monthly compounded interest on a loan of ${loan_amount} at {interest_rate}% yearly interest rate for {years} years is ${compounded_amount:.2f}.")
