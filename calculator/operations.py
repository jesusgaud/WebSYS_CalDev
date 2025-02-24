import importlib
import os
import sys
from decimal import Decimal
from typing import Protocol, Dict, Callable

# Define a protocol (interface) for mathematical operations
class Operation(Protocol):
    """Defines the interface for all mathematical operations."""
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        """Executes the operation on two operands."""
        pass

# Implementations for basic operations using the Command Pattern
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

# Dictionary to store all operations (built-in + plugins)
operations: Dict[str, Callable[[Decimal, Decimal], Decimal]] = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
}

# Dynamically load plugins
PLUGIN_DIR = os.path.join(os.path.dirname(__file__), "plugins")

def load_plugins():
    """Dynamically loads all operation plugins from the plugins directory."""
    if not os.path.exists(PLUGIN_DIR):
        os.makedirs(PLUGIN_DIR)  # Ensure the plugins directory exists

    sys.path.insert(0, PLUGIN_DIR)  # Add plugins directory to Python path

    for filename in os.listdir(PLUGIN_DIR):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = filename[:-3]  # Remove ".py" to get module name
            try:
                module = importlib.import_module(module_name)
                if hasattr(module, "operation"):
                    operations[module_name] = module.operation  # Register the plugin
                    print(f"Loaded plugin: {module_name}")  # Debugging log
            except Exception as e:
                print(f"Failed to load plugin {module_name}: {e}")

# Load plugins at startup
load_plugins()
