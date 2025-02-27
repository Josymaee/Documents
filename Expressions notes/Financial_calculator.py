# Josy Ramirez, Financial Calculator

def get_expenses():
    print("Hello! This is a financial calculator to help keep track of your money.")

    income = float(input("What is your income?\n"))
    rent = float(input("How much is your rent?\n"))
    utilities = float(input("How much are your utilities?\n"))
    groceries = float(input("How much are your groceries?\n"))
    transportation = float(input("How much is your transportation?\n"))

    return income, rent, utilities, groceries, transportation

def calculate_percentages(income, rent, utilities, groceries, transportation):
    savings = income * 0.10  # 10% of income
    spending = income - (savings + rent + utilities + groceries + transportation)

    # Calculate percentages
    rent_percent = (rent / income) * 100
    utilities_percent = (utilities / income) * 100
    groceries_percent = (groceries / income) * 100
    transportation_percent = (transportation / income) * 100
    savings_percent = (savings / income) * 100
    spending_percent = (spending / income) * 100

    # Print results
    print(f"\nFinancial Summary:")
    print(f"Your rent is ${rent:.2f}, which is {rent_percent:.2f}% of your income.")
    print(f"Your utilities are ${utilities:.2f}, which is {utilities_percent:.2f}% of your income.")
    print(f"Your groceries are ${groceries:.2f}, which is {groceries_percent:.2f}% of your income.")
    print(f"Your transportation is ${transportation:.2f}, which is {transportation_percent:.2f}% of your income.")
    print(f"Your savings are ${savings:.2f}, which is {savings_percent:.2f}% of your income.")
    print(f"Your remaining spending money is ${spending:.2f}, which is {spending_percent:.2f}% of your income.")

income, rent, utilities, groceries, transportation = get_expenses()
calculate_percentages(income, rent, utilities, groceries, transportation)
