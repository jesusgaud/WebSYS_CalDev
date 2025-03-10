"""Test main calculations using the Command Pattern"""

# Standard library imports
from decimal import Decimal, InvalidOperation

# Third-party imports
import pytest

# Application-specific imports
from app.calculation import Calculation
from app.operations import operations  # Import dynamically loaded operations

@pytest.mark.parametrize("a_string, b_string, operation_string, expected_string", [
    ("5", "3", "add", "The result of 5 add 3 is equal to 8"),
    ("10", "2", "subtract", "The result of 10 subtract 2 is equal to 8"),
    ("4", "5", "multiply", "The result of 4 multiply 5 is equal to 20"),
    ("20", "4", "divide", "The result of 20 divide 4 is equal to 5"),
    ("10", "3", "modulus", "The result of 10 modulus 3 is equal to 1"),  # Plugin test
    ("2", "3", "power", "The result of 2 power 3 is equal to 8"),  # Plugin test
    ("1", "0", "divide", "An error occurred: Cannot divide by zero"),
    ("9", "3", "unknown", "Unknown operation: unknown"),
    ("a", "3", "add", "Invalid number input: a or 3 is not a valid number."),
    ("5", "b", "subtract", "Invalid number input: 5 or b is not a valid number.")
])
def test_calculate_and_print(a_string, b_string, operation_string, expected_string, capsys):
    """Test Calculation operations, including dynamically loaded plugins."""

    try:
        # Convert inputs to Decimal
        a = Decimal(a_string)
        b = Decimal(b_string)

        # Validate operation
        if operation_string not in operations:
            raise AttributeError(f"Unknown operation: {operation_string}")

        operation_func = operations[operation_string]

        calc = Calculation(a, b, operation_func)
        result = calc.perform()
        print(f"The result of {a} {operation_string} {b} is equal to {result}")

    except InvalidOperation:
        print(f"Invalid number input: {a_string} or {b_string} is not a valid number.")
    except ZeroDivisionError:
        print("An error occurred: Cannot divide by zero")
    except AttributeError as e:
        print(str(e))

    # Capture output and validate
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_string
