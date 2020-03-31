class Vehicle:
    """A blueprint of vehicle entity"""

    def __init__(self, registration_number, color):
        """Construct a new Vehicle."""
        self._registration_number = registration_number
        self._color = color

    def get_registration_number(self):
        """Get the registration number of the vehicle."""
        return self._registration_number

    def get_color(self):
        """Get the color of the vehicle."""
        return self._color
