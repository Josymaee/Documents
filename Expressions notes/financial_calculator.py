# Josy Ramirez, Financial Calculator

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

# Calculate percentage of income spent on each category
rent_percent = (rent / income) * 100
utilities_percent = (utilities / income) * 100
groceries_percent = (groceries / income) * 100
transportation_percent = (transportation / income) * 100
savings_percent = (savings / income) * 100
spending_percent = (spending / income) * 100

# Display results
print("\n--- Financial Summary ---")
print(f"Your rent is ${rent:8f}, which is {rent_percent:.2f}% of your income.")
print(f"Your utilities are ${utilities:.2f}, which is {utilities_percent:.2f}% of your income.")
print(f"Your groceries cost ${groceries:.2f}, which is {groceries_percent:.2f}% of your income.")
print(f"Your transportation costs ${transportation:.2f}, which is {transportation_percent:.2f}% of your income.")
print(f"Your savings amount to ${savings:.2f}, which is {savings_percent:.2f}% of your income.")
print(f"Your spending money left is ${spending:.2f}, which is {spending_percent:.2f}% of your income.")
