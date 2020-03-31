from parking_lot.entities.vehicle import Vehicle
from parking_lot.entities.parking_lot import ParkingLot

from parking_lot.exceptions.no_available_slot import NoAvailableSlot
from parking_lot.exceptions.parking_lot_not_found import ParkingLotNotFound


class ParkingManager:
    """A blueprint of parking manager object"""

    def __init__(self):
        """Create a new parking manager instance."""
        self._parking_lot = None

    def create_parking_lot(self, total_slots):
        """Appends a ticket to the collection."""
        self._parking_lot = ParkingLot(int(total_slots))

        return f'Created a parking lot with {self._parking_lot.get_total_slots()} slots'

    def park(self, registration_number, colour):
        """Park the given vehicle in parking lot."""
        self._check_parking_lot_exists()

        try:
            vehicle = Vehicle(registration_number, colour)
            ticket = self._parking_lot.park(vehicle)

            return f'Allocated slot number: {ticket.get_slot().get_number()}'
        except NoAvailableSlot as e:
            return str(e)

    def leave(self, slot_number):
        """Leave the given slot number."""
        self._check_parking_lot_exists()

        ticket = self._parking_lot.unpark(int(slot_number))

        return f'Slot number {ticket.get_slot().get_number()} is free'

    def status(self):
        """Get status of parking lot."""
        self._check_parking_lot_exists()

        return [['Slot No.', 'Registration No', 'Colour']] + [
            [str(ticket.get_slot().get_number()), ticket.get_vehicle().get_registration_number(), ticket.get_vehicle().get_colour()]
            for ticket in self._parking_lot.get_issued_tickets()
        ]

    def registration_numbers_for_cars_with_colour(self, colour):
        """Get registration numbers of given colour of vehicle."""
        self._check_parking_lot_exists()

        tickets = self._parking_lot.filter_tickets_by_colour(colour)

        if tickets:
            return ', '.join(
                [ticket.get_vehicle().get_registration_number() for ticket in tickets]
            )

        return 'Not found'

    def slot_numbers_for_cars_with_colour(self, colour):
        """Get slot numbers of given colour of vehicle."""
        self._check_parking_lot_exists()

        tickets = self._parking_lot.filter_tickets_by_colour(colour)

        if tickets:
            return ', '.join([str(ticket.get_slot().get_number()) for ticket in tickets])

        return 'Not found'

    def slot_number_for_registration_number(self, registration_number):
        """Get slot number of given registration number of vehicle."""
        self._check_parking_lot_exists()

        ticket = self._parking_lot.find_ticket_by_registration_number(registration_number)

        return ticket.get_slot().get_number() if ticket else 'Not found'

    def _check_parking_lot_exists(self):
        if not self._parking_lot:
            raise ParkingLotNotFound

        return True