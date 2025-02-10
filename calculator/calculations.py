class Calculations:
    """Manages a history of calculations."""

    history = []  # Class attribute to store past calculations

    @classmethod
    def add_calculation(cls, calculation):
        """
        Adds a calculation to the history.

        Args:
            calculation (Calculation): A Calculation instance to store.
        """
        cls.history.append(calculation)

    @classmethod
    def get_last_calculation(cls):
        """
        Retrieves the most recent calculation from history.

        Returns:
            Calculation or None: The latest Calculation instance, or None if history is empty.
        """
        return cls.history[-1] if cls.history else None

    @classmethod
    def clear_history(cls):
        """Clears all stored calculations from history."""
        cls.history.clear()
