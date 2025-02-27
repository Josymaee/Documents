# Josy Ramirez, Financial Calculator
def info(cost, income, type):
    perrent = cost/income *100
    print(f"Your {type} is ${cost:.2f} which is XX% of your income.")
# Print statement that welcomes users
print("Hello! This is a financial calculator to help keep track of your money.")

# Ask for user inputs
income = float(input("What is your income?\n"))
rent = float(input("How much is your rent?\n"))
utilities = float(input("How much are your utilities?\n"))
groceries = float(input("How much are your groceries?\n"))
transportation = float(input("How much is your transportation?\n"))

# Calculate savings as 10% of income
savings = income * 0.10

# Calculate remaining spending money after expenses and savings
spending = income - (savings + rent + utilities + groceries + transportation)

info(rent, income, "rent")
info(utilities, income, "utilities")
info(groceries, income, "groceries")
info(transportation, income, "transportation")
info(spending, income, "spending")