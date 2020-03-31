class Ticket:
    """A blueprint of ticket object"""

    def __init__(self, vehicle, slot):
        """Construct a new Ticket."""
        self._vehicle = vehicle
        self._slot = slot

    def get_vehicle(self):
        """Get the vehicle assigned to the ticket."""
        return self._vehicle

    def get_slot(self):
        """Get the slot assigned to the ticket."""
        return self._slot
