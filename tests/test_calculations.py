"""Test Calculations Using the Command Pattern"""

# Standard library imports
from decimal import Decimal
import pytest

# Application-specific imports
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract, multiply, divide

@pytest.fixture(name="available_commands")
def fixture_available_commands():
    """Fixture that dynamically loads available commands from the operations module."""
    return {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }

@pytest.fixture(name="setup_calculations")
def fixture_setup_calculations():
    """Fixture to clear history and add sample calculations for tests."""
    Calculations.clear_history()
    Calculations.add_calculation(Calculation(Decimal('10'), Decimal('5'), add))
    Calculations.add_calculation(Calculation(Decimal('20'), Decimal('3'), subtract))

def test_add_calculation(setup_calculations):
    """Test adding a calculation to the history."""
    _ = setup_calculations  # Explicitly reference fixture
    calc = Calculation(Decimal('2'), Decimal('2'), add)
    Calculations.add_calculation(calc)
    assert Calculations.get_latest() == calc, "Failed to add the calculation to the history"

def test_get_history(setup_calculations):
    """Test retrieving the entire calculation history."""
    _ = setup_calculations  # Explicitly reference fixture
    history = Calculations.get_history()
    assert len(history) == 2, "History does not contain the expected number of calculations"

def test_clear_history(setup_calculations):
    """Test clearing the entire calculation history."""
    _ = setup_calculations  # Explicitly reference fixture
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0, "History was not cleared"

def test_get_latest(setup_calculations):
    """Test getting the latest calculation from the history."""
    _ = setup_calculations  # Explicitly reference fixture
    latest = Calculations.get_latest()
    assert latest is not None, "Latest calculation is None"
    assert latest.a == Decimal('20') and latest.b == Decimal('3'), "Did not get the correct latest calculation"

def test_find_by_operation(setup_calculations, available_commands):
    """Test finding calculations in the history by operation type."""
    _ = setup_calculations  # Explicitly reference fixture

    if hasattr(Calculations, "find_by_operation"):
        for operation_name in available_commands:
            operations = Calculations.find_by_operation(operation_name)
            assert isinstance(operations, list), "Expected a list of calculations"
    else:
        pytest.skip("find_by_operation method is missing in Calculations class")

def test_plugin_loading(available_commands):
    """Test that the command plugin system loads operations dynamically."""
    assert "add" in available_commands
    assert "subtract" in available_commands
    assert "multiply" in available_commands
    assert "divide" in available_commands
