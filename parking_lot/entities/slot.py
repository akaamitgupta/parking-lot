class Slot:
    """A blueprint of slot object"""

    def __init__(self, number):
        """Construct a new Slot."""
        self._number = number
        self._available = True

    def get_number(self):
        """Get the slot number."""
        return self._number

    def is_available(self):
        """Check of the slot is available."""
        return self._available

    def mark_available(self):
        """Marks the slot available."""
        self._available = True

    def mark_unavailable(self):
        """Marks the slot unavailable."""
        self._available = False
