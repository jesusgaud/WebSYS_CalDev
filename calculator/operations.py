from decimal import Decimal
from typing import Protocol

class Operation(Protocol):
    """Defines the interface for all mathematical operations."""
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        """Executes the operation on two operands."""
        pass

class AddOperation:
    """Command for addition."""
    @staticmethod
    def execute(a: Decimal, b: Decimal) -> Decimal:
        return a + b

class SubtractOperation:
    """Command for subtraction."""
    @staticmethod
    def execute(a: Decimal, b: Decimal) -> Decimal:
        return a - b

class MultiplyOperation:
    """Command for multiplication."""
    @staticmethod
    def execute(a: Decimal, b: Decimal) -> Decimal:
        return a * b

class DivideOperation:
    """Command for division."""
    @staticmethod
    def execute(a: Decimal, b: Decimal) -> Decimal:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

# Function-based operations (for compatibility)
def add(a: Decimal, b: Decimal) -> Decimal:
    """Performs addition"""
    return AddOperation.execute(a, b)

def subtract(a: Decimal, b: Decimal) -> Decimal:
    """Performs subtraction"""
    return SubtractOperation.execute(a, b)

def multiply(a: Decimal, b: Decimal) -> Decimal:
    """Performs multiplication"""
    return MultiplyOperation.execute(a, b)

def divide(a: Decimal, b: Decimal) -> Decimal:
    """Performs division"""
    return DivideOperation.execute(a, b)
