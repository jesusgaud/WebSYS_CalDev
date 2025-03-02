"""Test Operations with Dynamic Plugin Support"""

# Standard library imports
from decimal import Decimal
import pytest

# Application-specific imports
from app.calculation import Calculation
from app.operations import operations  # Import dynamically loaded operations

@pytest.mark.parametrize(
    "x, y, op_name, expected_result",
    [
        (Decimal("10"), Decimal("5"), "add", Decimal("15")),
        (Decimal("10"), Decimal("5"), "subtract", Decimal("5")),
        (Decimal("3"), Decimal("4"), "multiply", Decimal("12")),
        (Decimal("20"), Decimal("5"), "divide", Decimal("4")),
        (Decimal("10"), Decimal("3"), "modulus", Decimal("1")),  # Plugin test for modulus
        (Decimal("2"), Decimal("3"), "power", Decimal("8")),  # Plugin test for power
    ],
)
def test_operation(x, y, op_name, expected_result):
    """Test various operations, including dynamically loaded plugins."""
    assert op_name in operations, f"Operation '{op_name}' is not registered"

    # Retrieve function dynamically
    op_function = operations[op_name]

    # Use Calculation.create() if available
    calculation = Calculation.create(x, y, op_function)

    assert calculation.perform() == expected_result, f"{op_name} operation failed"


def test_divide_by_zero():
    """Ensure divide-by-zero raises an error."""
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        operations["divide"](Decimal(5), Decimal(0))


def test_plugin_discovery():
    """Ensure dynamically loaded plugins are discovered."""
    expected_plugins = ["modulus", "power"]
    for plugin in expected_plugins:
        assert plugin in operations, f"Plugin '{plugin}' was not loaded"

    # Explicitly check that functions are callable
    assert callable(operations["modulus"]), "Modulus operation is not callable"
    assert callable(operations["power"]), "Power operation is not callable"
