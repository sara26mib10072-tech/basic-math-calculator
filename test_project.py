# tests/test_project.py
# Plain Python test script using assert statements only.
# No external testing frameworks (unittest/pytest) are used.

import os
import sys

# Ensure the project root directory is accessible in the module search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from calculator import Calculator
from operations import (
    MENU_CHOICES,
    VALID_CHOICES_SET,
    OPERATION_NAMES,
    ZERO_CHECK_CHOICES,
    is_valid_number,
    parse_number,
    demonstrate_precedence
)


def test_addition():
    calc = Calculator()
    # Integer addition
    assert calc.add(10, 5) == 15
    # Float addition
    assert calc.add(2.5, 4.5) == 7.0
    # Negative number addition
    assert calc.add(-10, 4) == -6
    print("[PASS] test_addition passed")


def test_subtraction():
    calc = Calculator()
    # Integer subtraction
    assert calc.subtract(20, 8) == 12
    # Negative result
    assert calc.subtract(5, 12) == -7
    # Float subtraction
    assert calc.subtract(10.5, 2.5) == 8.0
    print("[PASS] test_subtraction passed")


def test_multiplication():
    calc = Calculator()
    # Integer multiplication
    assert calc.multiply(6, 7) == 42
    # Multiply by zero
    assert calc.multiply(15, 0) == 0
    # Float multiplication
    assert calc.multiply(2.5, 4) == 10.0
    print("[PASS] test_multiplication passed")


def test_division():
    calc = Calculator()
    # True division (always yields float)
    assert calc.divide(10, 4) == 2.5
    assert calc.divide(8, 2) == 4.0
    assert type(calc.divide(8, 2)) is float
    # Division by zero returns None
    assert calc.divide(10, 0) is None
    print("[PASS] test_division passed")


def test_floor_division():
    calc = Calculator()
    # Integer floor division
    assert calc.floor_divide(17, 5) == 3
    # Floor division by zero returns None
    assert calc.floor_divide(10, 0) is None
    print("[PASS] test_floor_division passed")


def test_modulus():
    calc = Calculator()
    # Modulus (remainder)
    assert calc.modulus(17, 5) == 2
    # Modulus by zero returns None
    assert calc.modulus(10, 0) is None
    print("[PASS] test_modulus passed")


def test_power():
    calc = Calculator()
    # Exponentiation
    assert calc.power(2, 3) == 8
    assert calc.power(5, 0) == 1
    assert calc.power(2.5, 2) == 6.25
    print("[PASS] test_power passed")


def test_identity_operator():
    calc = Calculator()
    # Division by zero returns None
    res_none = calc.divide(10, 0)
    assert res_none is None

    # Valid operation does not return None
    res_valid = calc.add(5, 5)
    assert res_valid is not None
    print("[PASS] test_identity_operator passed")


def test_input_validation():
    # Valid integers
    assert is_valid_number("42") is True
    assert is_valid_number("-15") is True
    assert is_valid_number("+7") is True
    assert is_valid_number("0") is True

    # Valid floating-point numbers
    assert is_valid_number("3.1415") is True
    assert is_valid_number("-0.75") is True
    assert is_valid_number("10.0") is True

    # Invalid non-numeric strings
    assert is_valid_number("hello") is False
    assert is_valid_number("12a") is False
    assert is_valid_number("1.2.3") is False
    assert is_valid_number("") is False
    assert is_valid_number("   ") is False
    assert is_valid_number("-") is False
    assert is_valid_number(".") is False
    print("[PASS] test_input_validation passed")


def test_parsing():
    # Integer parsing
    val_int = parse_number("42")
    assert val_int == 42
    assert type(val_int) is int

    # Float parsing
    val_float = parse_number("3.14")
    assert val_float == 3.14
    assert type(val_float) is float
    print("[PASS] test_parsing passed")


def test_data_structures():
    # Verify tuple
    assert type(MENU_CHOICES) is tuple
    assert len(MENU_CHOICES) == 8

    # Verify set
    assert type(VALID_CHOICES_SET) is set
    assert 1 in VALID_CHOICES_SET
    assert 8 in VALID_CHOICES_SET
    assert 9 not in VALID_CHOICES_SET

    # Verify dictionary
    assert type(OPERATION_NAMES) is dict
    assert OPERATION_NAMES[1] == "Addition"
    assert OPERATION_NAMES[8] == "Exit"

    # Verify frozenset
    assert type(ZERO_CHECK_CHOICES) is frozenset
    assert 4 in ZERO_CHECK_CHOICES  # Division
    assert 5 in ZERO_CHECK_CHOICES  # Floor division
    assert 6 in ZERO_CHECK_CHOICES  # Modulus
    assert 1 not in ZERO_CHECK_CHOICES  # Addition
    print("[PASS] test_data_structures passed")


def test_calculator_class_and_array():
    calc = Calculator()
    assert calc.calculation_count == 0
    assert len(calc.results_history) == 0

    # Record first result
    calc.record_result(15.5)
    assert calc.calculation_count == 1
    assert calc.last_result == 15.5
    assert len(calc.results_history) == 1
    assert calc.results_history[0] == 15.5

    # Record second result
    calc.record_result(30.0)
    assert calc.calculation_count == 2
    assert calc.last_result == 30.0
    assert len(calc.results_history) == 2
    assert calc.results_history[1] == 30.0

    # Test get_history
    history_list = calc.get_history()
    assert type(history_list) is list
    assert history_list == [15.5, 30.0]

    # Test clear_history
    calc.clear_history()
    assert calc.calculation_count == 0
    assert len(calc.results_history) == 0
    print("[PASS] test_calculator_class_and_array passed")


def test_operator_precedence():
    without_parens, with_parens = demonstrate_precedence(2, 3, 4)
    # 2 + 3 * 4 = 2 + 12 = 14 (multiplication before addition)
    assert without_parens == 14
    # (2 + 3) * 4 = 5 * 4 = 20 (parentheses override precedence)
    assert with_parens == 20
    assert without_parens != with_parens
    print("[PASS] test_operator_precedence passed")


def run_all_tests():
    print("========================================")
    print("Running Basic Math Calculator Test Suite")
    print("========================================")
    test_addition()
    test_subtraction()
    test_multiplication()
    test_division()
    test_floor_division()
    test_modulus()
    test_power()
    test_identity_operator()
    test_input_validation()
    test_parsing()
    test_data_structures()
    test_calculator_class_and_array()
    test_operator_precedence()
    print("========================================")
    print("All tests passed successfully! (13/13)")
    print("========================================")


if __name__ == "__main__":
    run_all_tests()
