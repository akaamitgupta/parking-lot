class Vehicle:
    """A blueprint of vehicle entity"""

    def __init__(self, registration_number, colour):
        """Construct a new Vehicle."""
        self._registration_number = registration_number
        self._colour = colour

    def get_registration_number(self):
        """Get the registration number of the vehicle."""
        return self._registration_number

    def get_colour(self):
        """Get the colour of the vehicle."""
        return self._colour
