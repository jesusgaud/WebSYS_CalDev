import sys
from calculator import Calculator
from decimal import Decimal, InvalidOperation
from calculator.operations import add, subtract, multiply, divide

def calculate_and_print(a, b, operation):
    """Performs an operation and prints result"""
    operations = {'add': add, 'subtract': subtract, 'multiply': multiply, 'divide': divide}

    if operation not in operations:
        print(f"Unknown operation: {operation}")
        return

    try:
        result = operations[operation](Decimal(a), Decimal(b))
        print(f"The result of {a} {operation} {b} is equal to {result}")
    except ZeroDivisionError:
        print("An error occurred: Cannot divide by zero")
    except ValueError:
        print(f"Invalid number input: {a} or {b} is not a valid number.")


def main():
    if len(sys.argv) != 4:
        print("Usage: python calculator_main.py <number1> <number2> <operation>")
        sys.exit(1)
    
    _, a, b, operation = sys.argv
    calculate_and_print(a, b, operation)

if __name__ == '__main__':
    main()