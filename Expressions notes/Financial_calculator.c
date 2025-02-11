// Josy Ramirez, financial calculator C

#include <stdio.h>

int main() {
    // Declare variables
    float income, rent, utilities, groceries, transportation;
    float savings, spending;
    float rent_percent, utilities_percent, groceries_percent, transportation_percent, savings_percent, spending_percent;

    // Print welcome message
    printf("Hello! This is a financial calculator to help keep track of your money.\n");

    // Ask for user inputs
    printf("What is your income?\n");
    scanf("%f", &income);

    printf("How much is your rent?\n");
    scanf("%f", &rent);

    printf("How much are your utilities?\n");
    scanf("%f", &utilities);

    printf("How much are your groceries?\n");
    scanf("%f", &groceries);

    printf("How much is your transportation?\n");
    scanf("%f", &transportation);

    // Calculate savings as 10% of income
    savings = income * 0.10;

    // Calculate remaining spending money after expenses and savings
    spending = income - (savings + rent + utilities + groceries + transportation);

    // Calculate percentage of income spent on each category
    rent_percent = (rent / income) * 100;
    utilities_percent = (utilities / income) * 100;
    groceries_percent = (groceries / income) * 100;
    transportation_percent = (transportation / income) * 100;
    savings_percent = (savings / income) * 100;
    spending_percent = (spending / income) * 100;

    // Display results
    printf("\n--- Financial Summary ---\n");
    printf("Your rent is $%.2f, which is %.2f%% of your income.\n", rent, rent_percent);
    printf("Your utilities are $%.2f, which is %.2f%% of your income.\n", utilities, utilities_percent);
    printf("Your groceries cost $%.2f, which is %.2f%% of your income.\n", groceries, groceries_percent);
    printf("Your transportation costs $%.2f, which is %.2f%% of your income.\n", transportation, transportation_percent);
    printf("Your savings amount to $%.2f, which is %.2f%% of your income.\n", savings, savings_percent);
    printf("Your spending money left is $%.2f, which is %.2f%% of your income.\n", spending, spending_percent);
}
