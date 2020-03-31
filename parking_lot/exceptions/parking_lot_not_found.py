class ParkingLotNotFound(Exception):
    """Raised when the there is no parking lot found."""

    def __init__(self):
        Exception.__init__(self, 'No parking lot found. Please create it before using.')
