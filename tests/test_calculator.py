"""Test Calculator Operations with Dynamic Plugin Support"""

# Standard library imports
from decimal import Decimal
import pytest

# Application-specific imports
from app.calculator import Calculator
from app.calculations import Calculations
from app.operations import operations  # Dynamically loaded operations

@pytest.fixture(name="clear_history_fixture")
def fixture_clear_history():
    """Fixture to clear calculation history before each test."""
    Calculations.clear_history()

@pytest.mark.usefixtures("clear_history_fixture")
def test_addition():
    """Test addition using the calculator"""
    assert Calculator.add(Decimal(2), Decimal(2)) == Decimal(4)
    assert len(Calculations.history) == 1

@pytest.mark.usefixtures("clear_history_fixture")
def test_subtraction():
    """Test subtraction using the calculator"""
    assert Calculator.subtract(Decimal(5), Decimal(3)) == Decimal(2)
    assert len(Calculations.history) == 1

@pytest.mark.usefixtures("clear_history_fixture")
def test_multiplication():
    """Test multiplication using the calculator"""
    assert Calculator.multiply(Decimal(3), Decimal(4)) == Decimal(12)
    assert len(Calculations.history) == 1

@pytest.mark.usefixtures("clear_history_fixture")
def test_division():
    """Test division using the calculator"""
    assert Calculator.divide(Decimal(10), Decimal(2)) == Decimal(5)
    assert len(Calculations.history) == 1

@pytest.mark.usefixtures("clear_history_fixture")
def test_divide_by_zero():
    """Test division by zero raises ZeroDivisionError"""
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        Calculator.divide(Decimal(5), Decimal(0))

@pytest.mark.usefixtures("clear_history_fixture")
def test_plugin_operations():
    """Test that dynamically loaded plugin operations work correctly."""
    assert "modulus" in operations
    assert "power" in operations
    assert operations["modulus"](Decimal(10), Decimal(3)) == Decimal(10) % Decimal(3)
    assert operations["power"](Decimal(2), Decimal(3)) == Decimal(2) ** Decimal(3)
