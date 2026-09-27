# operations.py
# This module provides supporting constants and helper functions for the calculator.

# Tuple storing menu options in fixed sequence (demonstrates tuple)
MENU_CHOICES = (1, 2, 3, 4, 5, 6, 7, 8)

# Set containing valid menu choice numbers for fast membership testing (demonstrates set)
VALID_CHOICES_SET = {1, 2, 3, 4, 5, 6, 7, 8}

# Dictionary mapping menu choice numbers to operation names (demonstrates dictionary)
OPERATION_NAMES = {
    1: "Addition",
    2: "Subtraction",
    3: "Multiplication",
    4: "Division",
    5: "Floor Division",
    6: "Modulus",
    7: "Power",
    8: "Exit"
}

# Frozen set of operations that require a non-zero divisor check (demonstrates frozenset)
# Operations 4 (Division), 5 (Floor Division), and 6 (Modulus) cannot have 0 as divisor.
ZERO_CHECK_CHOICES = frozenset([4, 5, 6])


def is_valid_number(text):
    """
    Validates whether a given string represents a valid integer or float.
    Uses basic string inspection without try/except.
    """
    cleaned = text.strip()

    # Empty string is not a valid number
    if len(cleaned) == 0:
        return False

    # Handle optional leading negative or positive sign
    if cleaned.startswith("-") or cleaned.startswith("+"):
        cleaned = cleaned[1:]

    # A sign alone (e.g. "-" or "+") is not a valid number
    if len(cleaned) == 0:
        return False

    # Check for decimal points
    dot_count = cleaned.count(".")
    if dot_count > 1:
        return False

    if dot_count == 1:
        # String has one decimal point (floating-point number)
        parts = cleaned.split(".")
        left = parts[0]
        right = parts[1]

        # Both sides cannot be empty (e.g., "." is invalid)
        if len(left) == 0 and len(right) == 0:
            return False

        # Left of decimal must be digits if present
        if len(left) > 0 and not left.isdigit():
            return False

        # Right of decimal must be digits if present
        if len(right) > 0 and not right.isdigit():
            return False

        return True
    else:
        # String has no decimal point (integer)
        return cleaned.isdigit()


def parse_number(text):
    """
    Converts a validated string into either an int or float.
    Demonstrates type conversion.
    """
    cleaned = text.strip()
    if "." in cleaned:
        return float(cleaned)
    else:
        return int(cleaned)


def display_menu():
    """Displays the main calculator menu to the user in the terminal."""
    print("\n=================================")
    print("      BASIC MATH CALCULATOR      ")
    print("=================================")
    print(" 1. Addition")
    print(" 2. Subtraction")
    print(" 3. Multiplication")
    print(" 4. Division")
    print(" 5. Floor Division")
    print(" 6. Modulus")
    print(" 7. Power")
    print(" 8. Exit")
    print("=================================")


def display_result(op_name, num1, num2, result):
    """
    Displays the calculation result along with operand details and data type.
    Demonstrates type() and string output.
    """
    print("\n---------------------------------")
    print("Operation : " + str(op_name))
    print("Number 1  : " + str(num1))
    print("Number 2  : " + str(num2))
    print("Result    : " + str(result))
    print("Type      : " + str(type(result)))
    print("---------------------------------")


def demonstrate_precedence(a, b, c):
    """
    Demonstrates operator precedence and associativity naturally:
    a + b * c vs (a + b) * c
    """
    without_brackets = a + b * c
    with_brackets = (a + b) * c
    return (without_brackets, with_brackets)
