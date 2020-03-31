class NoAvailableSlot(Exception):
    """Raised when the there is no available slots."""

    def __init__(self):
        Exception.__init__(self, 'Sorry, parking lot is full')
