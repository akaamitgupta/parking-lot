from parking_lot.entities.vehicle import Vehicle
from parking_lot.entities.parking_lot import ParkingLot

from parking_lot.exceptions.no_available_slot import NoAvailableSlot


class ParkingManager:
    """A blueprint of parking manager object"""

    def __init__(self):
        """Create a new parking manager instance."""
        self._parking_lot = None

    def create_parking_lot(self, total_slots):
        """Appends a ticket to the collection."""
        self._parking_lot = ParkingLot(int(total_slots))

        return f'Created a parking lot with {self._parking_lot.get_total_slots()} slots'

    def park(self, registration_number, color):
        """Park the given vehicle in parking lot."""
        try:
            vehicle = Vehicle(registration_number, color)
            ticket = self._parking_lot.park(vehicle)

            return f'Allocated slot number: {ticket.get_slot().get_number()}'
        except NoAvailableSlot as e:
            return str(e)

    def leave(self, slot_number):
        """Leave the given slot number."""
        ticket = self._parking_lot.unpark(int(slot_number))

        return f'Slot number {ticket.get_slot().get_number()} is free'

