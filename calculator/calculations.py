class Calculations:
    history = []

    @classmethod
    def add_calculation(cls, calculation):
        """Adds a calculation to history"""
        cls.history.append(calculation)

    @classmethod
    def get_latest(cls):
        """Returns the latest calculation"""
        return cls.history[-1] if cls.history else None

    @classmethod
    def get_history(cls):
        """Returns all calculation history"""
        return cls.history

    @classmethod
    def clear_history(cls):
        """Clears the calculation history"""
        cls.history.clear()

@staticmethod
def find_by_operation(operation: str):
    """Retrieve calculations filtered by operation."""
    return [calc for calc in Calculations.history if calc.operation.__name__ == operation]
