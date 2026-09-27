# main.py
# Main driver script for the Basic Math Calculator project.

from calculator import Calculator
from operations import (
    MENU_CHOICES,
    VALID_CHOICES_SET,
    OPERATION_NAMES,
    ZERO_CHECK_CHOICES,
    is_valid_number,
    parse_number,
    display_menu,
    display_result
)


def get_number_input(prompt_text):
    """
    Safely retrieves a valid number (integer or float) from the user.
    Uses while loop and string validation instead of try/except.
    """
    while True:
        raw_input = input(prompt_text).strip()
        # Validate that the entered string is a valid numeric value
        if is_valid_number(raw_input):
            return parse_number(raw_input)
        else:
            print("Invalid input! Please enter a valid integer or floating-point number.")


def main():
    """
    Main function that runs the calculator program loop.
    Controls menu display, user input, operation dispatch, and results.
    """
    # Create an instance of the Calculator class
    calc = Calculator()

    # List to store calculation history records as tuples (demonstrates list and tuple)
    history_records = []

    print("Welcome to the Basic Math Calculator!")

    # Program loop to keep the calculator running until the user chooses to exit
    while True:
        # Display the calculator menu
        display_menu()

        # Prompt the user for an operation choice
        choice_text = input("Enter your choice (1-8): ").strip()

        # Check if the input is a valid integer choice
        if not is_valid_number(choice_text):
            print("Invalid choice! Please enter a number between 1 and 8.")
            continue

        choice = parse_number(choice_text)

        # Validate menu choice using set membership operator 'not in'
        if choice not in VALID_CHOICES_SET:
            print("Invalid choice! Please select an option between 1 and 8.")
            continue

        # Exit option (Option 8)
        if choice == 8:
            print("\nExiting Basic Math Calculator...")
            print("Total calculations performed: " + str(calc.calculation_count))
            print("Thank you for using the calculator. Goodbye!")
            break

        # Retrieve operation name from dictionary mapping
        op_name = OPERATION_NAMES[choice]
        print("\nSelected Operation: " + op_name)

        # Ask the user for the two numbers
        num1 = get_number_input("Enter the first number: ")
        num2 = get_number_input("Enter the second number: ")

        # Check for division by zero before performing division operations
        # Uses membership operator 'in', logical operator 'and', relational '=='
        if (choice in ZERO_CHECK_CHOICES) and (num2 == 0):
            print("\nError: Division by zero is not allowed for " + op_name + "!")
            continue

        # Perform the selected arithmetic operation using if/elif/else
        result = None

        if choice == 1:
            result = calc.add(num1, num2)
        elif choice == 2:
            result = calc.subtract(num1, num2)
        elif choice == 3:
            result = calc.multiply(num1, num2)
        elif choice == 4:
            result = calc.divide(num1, num2)
        elif choice == 5:
            result = calc.floor_divide(num1, num2)
        elif choice == 6:
            result = calc.modulus(num1, num2)
        elif choice == 7:
            result = calc.power(num1, num2)

        # Identity operator check: verifies whether result is None
        if result is None:
            print("\nError: The operation could not be completed.")
        else:
            # Record result in calculator state (updates count and array history)
            calc.record_result(result)

            # Store the calculation record as a tuple inside the history list
            history_records.append((op_name, num1, num2, result))

            # Display the formatted result and its data type
            display_result(op_name, num1, num2, result)

        # Ask the user if they wish to perform another calculation
        user_continue = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
        if user_continue == "no" or user_continue == "n":
            print("\nExiting Basic Math Calculator...")
            print("Total calculations performed: " + str(calc.calculation_count))
            print("Thank you for using the calculator. Goodbye!")
            break


if __name__ == "__main__":
    main()
