// Josy Ramirez, Financial Calculator C

#include <stdio.h>

// Function to get valid positive input from the user
double get_positive_input(char prompt[]) {
    double value;
    while (1) {
        printf("%s", prompt);
        if (scanf("%lf", &value) != 1) {
            printf("Invalid input. Please enter a numerical value.\n");
            while (getchar() != '\n'); // Clear input buffer
        } else if (value < 0) {
            printf("Expense cannot be negative. Please enter a valid amount.\n");
        } else {
            return value;
        }
    }
}

// Function to get user income and expenses
void get_expenses(double *income, double *rent, double *utilities, double *groceries, double *transportation) {
    printf("Hello! This is a financial calculator to help keep track of your money.\n\n");

    while (1) {
        printf("What is your income?\n");
        if (scanf("%lf", income) != 1 || *income <= 0) {
            printf("Income must be greater than zero. Please enter a valid amount.\n");
            while (getchar() != '\n'); // Clear input buffer
        } else {
            break;
        }
    }

    *rent = get_positive_input("How much is your rent?\n");
    *utilities = get_positive_input("How much are your utilities?\n");
    *groceries = get_positive_input("How much are your groceries?\n");
    *transportation = get_positive_input("How much is your transportation?\n");
}

// Function to calculate percentages and display results
void calculate_percentages(double income, double rent, double utilities, double groceries, double transportation) {
    double savings = income * 0.10;  // 10% of income
    double spending = income - (savings + rent + utilities + groceries + transportation);

    // Calculate percentages
    double rent_percent = (rent / income) * 100;
    double utilities_percent = (utilities / income) * 100;
    double groceries_percent = (groceries / income) * 100;
    double transportation_percent = (transportation / income) * 100;
    double savings_percent = (savings / income) * 100;
    double spending_percent = (spending / income) * 100;

    // Print financial summary
    printf("\n------ Financial Summary ------\n");
    printf("Your rent is $%.2f, which is %.2f%% of your income.\n", rent, rent_percent);
    printf("Your utilities are $%.2f, which is %.2f%% of your income.\n", utilities, utilities_percent);
    printf("Your groceries are $%.2f, which is %.2f%% of your income.\n", groceries, groceries_percent);
    printf("Your transportation is $%.2f, which is %.2f%% of your income.\n", transportation, transportation_percent);
    printf("Your savings are $%.2f, which is %.2f%% of your income.\n", savings, savings_percent);
    printf("Your remaining spending money is $%.2f, which is %.2f%% of your income.\n", spending, spending_percent);
    printf("--------------------------------\n");
}

// Main function
int main() {
    double income, rent, utilities, groceries, transportation;
    get_expenses(&income, &rent, &utilities, &groceries, &transportation);
    calculate_percentages(income, rent, utilities, groceries, transportation);

    return 0;
}
