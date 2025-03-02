# conftest.py
from decimal import Decimal
import pytest
from faker import Faker
from app.operations import operations  # Import dynamically loaded operations

fake = Faker()

def generate_test_data(num_records):
    """Generates test data dynamically, including plugin operations."""

    for _ in range(num_records):
        a = Decimal(fake.random_number(digits=2))
        b = Decimal(fake.random_number(digits=2)) if _ % 4 != 3 else Decimal(1)
        operation_name = fake.random_element(elements=list(operations.keys()))
        operation_func = operations[operation_name]

        # Ensure `b` is never zero when division is tested
        if operation_name == "divide" and b == Decimal(0):
            b = Decimal(1)

        try:
            expected = operation_func(a, b)
        except ZeroDivisionError:
            expected = "ZeroDivisionError"

        yield a, b, operation_name, operation_func, expected

def pytest_addoption(parser):
    """Adds custom command-line options for test configuration."""
    parser.addoption("--num_records", action="store", default=5, type=int,
                     help="Number of test records to generate")

@pytest.fixture
def operations_fixture():
    """Fixture that returns available operations."""
    return operations  # Uses dynamically loaded operations

def pytest_generate_tests(metafunc):
    """Dynamically generates test cases for operations, including plugins."""
    if {"a", "b", "expected"}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption("num_records")
        parameters = list(generate_test_data(num_records))

        metafunc.parametrize(
            "a,b,operation,expected",
            [
                (a, b, op_name if "operation_name" in metafunc.fixturenames else op_func, expected)
                for a, b, op_name, op_func, expected in parameters
            ]
        )
