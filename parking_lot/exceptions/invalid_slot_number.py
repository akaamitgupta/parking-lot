class InvalidSlotNumber(Exception):
    """Raised when the given slot number is invalid."""

    def __init__(self):
        Exception.__init__(self, 'The given slot number is invalid')
