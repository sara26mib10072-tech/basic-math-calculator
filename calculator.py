# calculator.py
# This module defines the Calculator class for performing basic arithmetic operations.

import array


class Calculator:
    """
    A simple Calculator class that provides basic arithmetic operations
    and keeps track of calculation history using Python's array data structure.
    """

    def __init__(self):
        # Total number of calculations performed during the session
        self.calculation_count = 0

        # Stores the most recent calculation result
        self.last_result = 0.0

        # array('d') stores numerical floating-point calculation results
        # 'd' represents double precision floating-point numbers
        self.results_history = array.array('d')

    def add(self, a, b):
        """Performs addition of two numbers: a + b"""
        return a + b

    def subtract(self, a, b):
        """Performs subtraction: a - b"""
        return a - b

    def multiply(self, a, b):
        """Performs multiplication: a * b"""
        return a * b

    def divide(self, a, b):
        """
        Performs true division: a / b
        Returns None if the divisor b is 0.
        """
        if b == 0:
            return None
        return a / b

    def floor_divide(self, a, b):
        """
        Performs floor division: a // b
        Returns None if the divisor b is 0.
        """
        if b == 0:
            return None
        return a // b

    def modulus(self, a, b):
        """
        Performs modulus (remainder): a % b
        Returns None if the divisor b is 0.
        """
        if b == 0:
            return None
        return a % b

    def power(self, a, b):
        """Performs exponentiation: a ** b"""
        return a ** b

    def record_result(self, result):
        """
        Updates the calculation count and stores the result in history.
        Demonstrates the assignment operator += and array manipulation.
        """
        self.calculation_count += 1
        self.last_result = float(result)
        self.results_history.append(float(result))

    def get_history(self):
        """Returns a list of all numeric results stored in the array."""
        return list(self.results_history)

    def clear_history(self):
        """Resets the calculator state and history."""
        self.calculation_count = 0
        self.last_result = 0.0
        self.results_history = array.array('d')
