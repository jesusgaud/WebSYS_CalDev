from decimal import Decimal

def add(a: Decimal, b: Decimal) -> Decimal:
    """Performs addition"""
    return a + b

def subtract(a: Decimal, b: Decimal) -> Decimal:
    """Performs subtraction"""
    return a - b

def multiply(a: Decimal, b: Decimal) -> Decimal:
    """Performs multiplication"""
    return a * b

def divide(a: Decimal, b: Decimal) -> Decimal:
    """Performs division"""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
