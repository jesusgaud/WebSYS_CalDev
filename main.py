"""Interactive Calculator Using the Command Pattern with Multiprocessing"""

import sys
import multiprocessing
from decimal import Decimal, InvalidOperation
from calculator.calculation import Calculation
from calculator.operations import operations  # Import dynamically loaded operations

def load_commands():
    """Dynamically loads available commands, including plugins."""
    return operations  # Return the entire operations dictionary, including dynamically loaded plugins

def calculate_and_print(a, b, operation):
    """Performs calculation in a separate process and prints the result."""
    commands = load_commands()

    if operation not in commands:
        print(f"Unknown operation: {operation}")
        return

    try:
        a = Decimal(a)
        b = Decimal(b)
        calc = Calculation(a, b, commands[operation])
        result = calc.perform()
        print(f"The result of {a} {operation} {b} is equal to {result}")
    except ZeroDivisionError:
        print("An error occurred: Cannot divide by zero")
    except InvalidOperation:
        print(f"Invalid number input: {a} or {b} is not a valid number.")

def execute_command(a, b, operation):
    """Executes a mathematical operation using multiprocessing."""
    process = multiprocessing.Process(target=calculate_and_print, args=(a, b, operation))
    process.start()
    process.join()  # Ensure the process completes before proceeding

def interactive_mode():
    """Runs the calculator in interactive REPL mode."""
    print("Welcome to the Interactive Calculator (type 'exit' to quit, 'menu' for available commands)")

    commands = load_commands()
    while True:
        user_input = input("\nEnter calculation (e.g., '5 3 add'): ").strip().lower()
        if user_input == "exit":
            print("Exiting calculator. Goodbye!")
            break
        elif user_input == "menu":
            print("\nAvailable commands:", ", ".join(commands.keys()))  # Shows dynamically loaded plugins
            continue

        parts = user_input.split()
        if len(parts) != 3:
            print("Invalid input. Use format: <number1> <number2> <operation>")
            continue

        a, b, operation = parts
        execute_command(a, b, operation)

def main():
    """Runs either interactive mode or command-line mode based on user input."""
    if len(sys.argv) == 1:
        interactive_mode()
    elif len(sys.argv) == 4:
        _, a, b, operation = sys.argv
        execute_command(a, b, operation)
    else:
        print("Usage: python main.py OR python main.py <number1> <number2> <operation>")
        sys.exit(1)

if __name__ == '__main__':
    multiprocessing.set_start_method("fork")  # Ensure multiprocessing compatibility
    main()
