class DuplicateVehicle(Exception):
    """Raised when the given vehicle is already parked."""

    def __init__(self):
        Exception.__init__(self, 'The given vehicle is already parked')
