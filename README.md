# Basic Math Calculator

A beginner-friendly, modular command-line calculator developed strictly using fundamental Python concepts. This project is tailored for a first-year **Python Essentials** course, demonstrating core language fundamentals, procedural control flow, data structures, and basic object-oriented programming without relying on external libraries or complex frameworks.

---

## Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Course Concepts Demonstrated](#course-concepts-demonstrated)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation and Setup](#installation-and-setup)
- [Running the Project](#running-the-project)
- [Running the Tests](#running-the-tests)
- [Example Terminal Sessions](#example-terminal-sessions)
- [Manual Testing Guide](#manual-testing-guide)
- [Limitations](#limitations)

---

## Project Description

The **Basic Math Calculator** is an interactive console application that performs common arithmetic operations on user-provided integers or floating-point numbers. It guides the user through an intuitive numeric menu, collects operands with custom input validation, protects against division-by-zero runtime errors, and logs numerical results into an in-memory session history using Python's standard `array` data structure.

---

## Features

- **Addition (`+`)**: Adds two numbers (integers or floats).
- **Subtraction (`-`)**: Computes the difference between two numbers.
- **Multiplication (`*`)**: Multiplies two numbers.
- **True Division (`/`)**: Calculates precise floating-point quotient.
- **Floor Division (`//`)**: Calculates integer quotient truncated toward negative infinity.
- **Modulus (`%`)**: Computes the remainder of division.
- **Power (`**`)**: Computes base raised to the exponent.
- **Division-by-Zero Protection**: Validates zero divisors for division, floor division, and modulus operations before evaluation.
- **Exception-Free Input Validation**: Validates integer and floating-point inputs using string inspection without `try/except` statements.
- **Session Results Tracking**: Tracks total calculation counts and stores numerical floating-point results in a standard library `array`.
- **Dynamic Type Inspection**: Displays the output data type (`<class 'int'>` or `<class 'float'>`) using Python's built-in `type()` function.

---

## Course Concepts Demonstrated

This project adheres strictly to the approved first-year Python syllabus and demonstrates each concept naturally:

| Concept | Implementation in Code |
| :--- | :--- |
| **I/O Operations** | `print()` for formatted menus and outputs; `input()` for interactive user intake. |
| **Variables & Types** | `int`, `float`, `str`, `bool`, and dynamic type inspection with `type()`. |
| **Arithmetic Operators** | `+`, `-`, `*`, `/`, `//`, `%`, `**` in `calculator.py`. |
| **Assignment Operators** | Simple assignment `=` and cumulative increment `+=` for `calculation_count`. |
| **Relational Operators** | `==`, `!=`, `<`, `>`, `<=`, `>=` for menu bounds, zero checks, and comparison tests. |
| **Logical Operators** | `and`, `or`, `not` for composite validation conditions and input evaluation. |
| **Membership Operators** | `in` and `not in` checking menu choices against `VALID_CHOICES_SET` and `ZERO_CHECK_CHOICES`. |
| **Identity Operators** | `is` and `is not` to canonically verify `result is None` when handling division by zero. |
| **Type Conversion** | Converting validated string inputs using `int()` and `float()` in `parse_number()`. |
| **Mixed Data Types** | Demonstrating float results from integer division (e.g. `10 / 4 = 2.5`). |
| **Operator Precedence** | Demonstrating standard evaluation order `a + b * c` versus `(a + b) * c`. |
| **Data Structures** | <ul><li>**List**: Storing session calculation records `history_records = []`.</li><li>**Tuple**: Immutable menu definition and log records `(op_name, num1, num2, result)`.</li><li>**Set**: Fast menu membership checking `VALID_CHOICES_SET = {1, 2, ..., 8}`.</li><li>**Dictionary**: Mapping choice IDs to operation titles `OPERATION_NAMES`.</li><li>**Frozen Set**: Immutable collection of operations requiring zero divisor checks: `ZERO_CHECK_CHOICES = frozenset([4, 5, 6])`.</li><li>**Array (`array('d')`)**: Python standard library array storing numerical float results.</li></ul> |
| **Control Flow** | `while` loops for continuous execution, `if/elif/else` branching, `break` for exit, and `continue` for re-prompting. |
| **Functions & Modules** | Modular design with separate modules (`main.py`, `calculator.py`, `operations.py`). |
| **Basic OOP** | `Calculator` class with constructor `__init__`, state attributes, and computation methods without complex inheritance or magic methods. |

---

## Project Structure

```text
basic-math-calculator/
│
├── README.md               # Complete project documentation and manual testing guide
├── main.py                 # Application driver containing the interactive menu loop
├── calculator.py           # Calculator class managing arithmetic methods and state
├── operations.py           # Helper validation functions, display logic, and data constants
└── tests/
    └── test_project.py     # Assert-based automated test suite (no external frameworks)
```

### Module Responsibilities:
- **`main.py`**: Handles user input, menu display, operation dispatch, session history, and exit flows.
- **`calculator.py`**: Defines the `Calculator` class with clean arithmetic methods (`add`, `subtract`, `multiply`, `divide`, `floor_divide`, `modulus`, `power`), result history recording, and internal state.
- **`operations.py`**: Houses reusable helper functions (`is_valid_number`, `parse_number`, `display_menu`, `display_result`, `demonstrate_precedence`) and course data structures (`MENU_CHOICES`, `VALID_CHOICES_SET`, `OPERATION_NAMES`, `ZERO_CHECK_CHOICES`).
- **`tests/test_project.py`**: Verifies program accuracy using plain Python `assert` statements across 13 distinct unit test functions.

---

## Requirements

- **Python 3.8 or higher**
- No external packages or third-party dependencies are required (`requirements.txt` is not needed).
- All functionality uses Python's built-in standard library (`array`, `sys`, `os`).

---

## Installation and Setup

1. **Verify Python Installation**:
   Ensure Python 3 is installed and available in your system path:
   ```bash
   python --version
   ```
   *(On macOS/Linux systems, use `python3 --version`)*

2. **Download or Clone the Repository**:
   Clone or copy the project files to your desired workspace directory:
   ```bash
   git clone <repository_url>
   cd basic-math-calculator
   ```

3. **Open Terminal in Project Directory**:
   Confirm that `main.py`, `calculator.py`, and `operations.py` are present in your active directory.

---

## Running the Project

To start the interactive calculator, run:

```bash
python main.py
```

*(On macOS or Linux systems if `python` points to Python 2, use:)*
```bash
python3 main.py
```

---

## Running the Tests

To verify calculations and logic without any third-party test runners, execute:

```bash
python tests/test_project.py
```

Expected output:
```text
========================================
Running Basic Math Calculator Test Suite
========================================
[PASS] test_addition passed
[PASS] test_subtraction passed
[PASS] test_multiplication passed
[PASS] test_division passed
[PASS] test_floor_division passed
[PASS] test_modulus passed
[PASS] test_power passed
[PASS] test_identity_operator passed
[PASS] test_input_validation passed
[PASS] test_parsing passed
[PASS] test_data_structures passed
[PASS] test_calculator_class_and_array passed
[PASS] test_operator_precedence passed
========================================
All tests passed successfully! (13/13)
========================================
```

---

## Example Terminal Sessions

### Session 1: Addition and Floating-Point Division

```text
Welcome to the Basic Math Calculator!

=================================
      BASIC MATH CALCULATOR      
=================================
 1. Addition
 2. Subtraction
 3. Multiplication
 4. Division
 5. Floor Division
 6. Modulus
 7. Power
 8. Exit
=================================
Enter your choice (1-8): 1

Selected Operation: Addition
Enter the first number: 12.5
Enter the second number: 7.5

---------------------------------
Operation : Addition
Number 1  : 12.5
Number 2  : 7.5
Result    : 20.0
Type      : <class 'float'>
---------------------------------

Do you want to perform another calculation? (yes/no): yes

=================================
      BASIC MATH CALCULATOR      
=================================
 1. Addition
 2. Subtraction
 3. Multiplication
 4. Division
 5. Floor Division
 6. Modulus
 7. Power
 8. Exit
=================================
Enter your choice (1-8): 4

Selected Operation: Division
Enter the first number: 10
Enter the second number: 4

---------------------------------
Operation : Division
Number 1  : 10
Number 2  : 4
Result    : 2.5
Type      : <class 'float'>
---------------------------------

Do you want to perform another calculation? (yes/no): no

Exiting Basic Math Calculator...
Total calculations performed: 2
Thank you for using the calculator. Goodbye!
```

### Session 2: Division by Zero Prevention

```text
=================================
      BASIC MATH CALCULATOR      
=================================
 1. Addition
 2. Subtraction
 3. Multiplication
 4. Division
 5. Floor Division
 6. Modulus
 7. Power
 8. Exit
=================================
Enter your choice (1-8): 4

Selected Operation: Division
Enter the first number: 25
Enter the second number: 0

Error: Division by zero is not allowed for Division!
```

---

## Manual Testing Guide

Use the following test cases to manually verify program functionality from the terminal:

| Test Case | Selected Option | Input 1 | Input 2 | Expected Result | Verified Behavior |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Addition** | 1 | `15` | `25` | `40` | Result type `<class 'int'>` |
| **Subtraction** | 2 | `20` | `35` | `-15` | Handles negative result |
| **Multiplication** | 3 | `4.5` | `2` | `9.0` | Mixed integer and float |
| **Division** | 4 | `15` | `2` | `7.5` | Exact float division |
| **Floor Division** | 5 | `17` | `5` | `3` | Truncated integer division |
| **Modulus** | 6 | `17` | `5` | `2` | Remainder calculation |
| **Power** | 7 | `2` | `8` | `256` | Exponentiation `2 ** 8` |
| **Zero Divisor** | 4, 5, or 6 | `50` | `0` | Division by zero error | Program rejects zero divisor gracefully |
| **Invalid Menu Option** | `9` or `abc` | - | - | Re-prompts user | Warns user and keeps running |
| **Invalid Number Input** | 1 | `abc` | `10` | Re-prompts for Number 1 | Safely prompts without crashing |
| **Exit Option** | 8 | - | - | Exits application | Shows total calculations count |

---

## Limitations

- **Terminal Environment Only**: Runs entirely in the command-line interface; does not include a GUI or web frontend.
- **Binary Operations**: Solves operations between two operands at a time.
- **Educational Scope**: Intentionally does not include trigonometric functions, logarithms, or imaginary/complex numbers to keep the code accessible for first-year engineering students.
