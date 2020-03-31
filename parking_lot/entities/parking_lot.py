from parking_lot.entities.slot import Slot


class ParkingLot:
    """A blueprint of parkinglot object"""

    def __init__(self, total_slots):
        """Construct a new ParkingLot."""
        self._slots = {number:Slot(number) for number in range(1, total_slots + 1)}
        self._total_slots = len(self._slots)
        self._available_slots = len(self._slots)

    def get_total_slots(self):
        """Get the total slots."""
        return self._total_slots

    def get_available_slots(self):
        """Get the total available slots."""
        return self._available_slots
