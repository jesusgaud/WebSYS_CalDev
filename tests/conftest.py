# conftest.py
from decimal import Decimal
from faker import Faker
import pytest
from calculator.operations import add, subtract, multiply, divide

fake = Faker()

# Centralized operations mapping (Avoid duplication in main.py and test_main.py)
def get_operations():
    """Returns a dictionary mapping operation names to functions."""
    return {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }

def generate_test_data(num_records):
    """Generates test data for both Calculator and Calculation tests."""
    operations_map = get_operations()

    for _ in range(num_records):
        a = Decimal(fake.random_number(digits=2))
        b = Decimal(fake.random_number(digits=2)) if _ % 4 != 3 else Decimal(1)
        operation_name = fake.random_element(elements=list(operations_map.keys()))
        operation_func = operations_map[operation_name]

        # Ensure `b` is never zero when division is tested
        if operation_func is divide and b == Decimal(0):
            b = Decimal(1)

        try:
            expected = operation_func(a, b)
        except ZeroDivisionError:
            expected = "ZeroDivisionError"

        yield a, b, operation_name, operation_func, expected

def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=5, type=int,
                     help="Number of test records to generate")

@pytest.fixture
def operations_fixture():
    """Fixture that returns available operations."""
    return get_operations()

def pytest_generate_tests(metafunc):
    """Dynamically generates test cases."""
    if {"a", "b", "expected"}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption("num_records")
        parameters = list(generate_test_data(num_records))

        modified_parameters = [
            (a, b, op_name if "operation_name" in metafunc.fixturenames else op_func, expected)
            for a, b, op_name, op_func, expected in parameters
        ]
        metafunc.parametrize("a,b,operation,expected", modified_parameters)
