"""
Day 2 - Interactive Calculator
Takes two numbers from user, performs basic arithmetic operations.
Demonstrates input(), type conversion, and f-strings.
"""


def get_number(prompt):
    """
    Get a valid number from user input.

    Args:
        prompt: str - message to display to the user

    Returns:
        float - validated number from user
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def calculate(first_number, second_number):
    """
    Perform all arithmetic operations on two numbers.

    Args:
        first_number: float
        second_number: float
    """
    print(f"\n--- Results ---")
    print(f"Addition:       {first_number} + {second_number} = {first_number + second_number}")
    print(f"Subtraction:    {first_number} - {second_number} = {first_number - second_number}")
    print(f"Multiplication: {first_number} * {second_number} = {first_number * second_number}")

    if second_number != 0:
        print(f"Division:       {first_number} / {second_number} = {first_number / second_number:.2f}")
    else:
        print("Division:       Cannot divide by zero")


first_number = get_number("Enter first number: ")
second_number = get_number("Enter second number: ")
calculate(first_number, second_number)