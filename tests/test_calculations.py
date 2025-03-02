"""Test Calculations Using the Command Pattern"""

# Standard library imports
from decimal import Decimal
import pytest

# Application-specific imports
from app.calculation import Calculation
from app.calculations import Calculations
from app.operations import operations  # Dynamically loaded operations

@pytest.fixture(name="setup_calculations")
def fixture_setup_calculations():
    """Fixture to clear history and add sample calculations for tests."""
    Calculations.clear_history()
    Calculations.add_calculation(Calculation(Decimal('10'), Decimal('5'), operations["add"]))
    Calculations.add_calculation(Calculation(Decimal('20'), Decimal('3'), operations["subtract"]))

def test_add_calculation(setup_calculations):
    """Test adding a calculation to the history."""
    _ = setup_calculations  # Explicitly reference fixture
    calc = Calculation(Decimal('2'), Decimal('2'), operations["add"])
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

def test_clear_history_multiple_times(setup_calculations):
    """Test calling clear_history multiple times."""
    _ = setup_calculations  # Explicitly reference fixture
    Calculations.clear_history()
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0, "History should remain empty after multiple clears"

def test_get_latest(setup_calculations):
    """Test getting the latest calculation from the history."""
    _ = setup_calculations  # Explicitly reference fixture
    latest = Calculations.get_latest()
    assert latest is not None, "Latest calculation is None"
    assert latest.a == Decimal('20') and latest.b == Decimal('3'), "Did not get the correct latest calculation"

def test_get_latest_empty_history():
    """Test getting the latest calculation when history is empty."""
    Calculations.clear_history()
    assert Calculations.get_latest() is None, "Expected None for latest calculation with empty history"

@pytest.mark.parametrize("operation_name", list(operations.keys()))
def test_find_by_operation(setup_calculations, operation_name):
    """Test finding calculations in the history by operation type."""
    _ = setup_calculations  # Explicitly reference fixture
    if hasattr(Calculations, "find_by_operation"):
        operations_found = Calculations.find_by_operation(operation_name)
        assert isinstance(operations_found, list), f"Expected a list for {operation_name}"
    else:
        pytest.skip("find_by_operation method is missing in Calculations class")

def test_find_by_operation_no_match(setup_calculations):
    """Test finding calculations when no match exists."""
    _ = setup_calculations  # Explicitly reference fixture
    results = Calculations.find_by_operation("non_existent_operation")
    assert results == [], "Expected empty list when no matching operation is found"

def test_plugin_loading():
    """Test that the command plugin system loads operations dynamically."""
    expected_operations = {"add", "subtract", "multiply", "divide", "modulus", "power"}
    for op in expected_operations:
        assert op in operations, f"Operation '{op}' was not loaded"
