from parking_lot.entities.slot import Slot
from parking_lot.entities.ticket import Ticket
from parking_lot.exceptions.no_available_slot import NoAvailableSlot
from parking_lot.exceptions.invalid_slot_number import InvalidSlotNumber


class ParkingLot:
    """A blueprint of parkinglot object"""

    def __init__(self, total_slots):
        """Construct a new ParkingLot."""
        self._slots = [Slot(number) for number in range(1, total_slots + 1)]
        self._total_slots = self._available_slots = total_slots
        self._issued_tickets = {}

    def get_total_slots(self):
        """Get the total slots."""
        return self._total_slots

    def get_available_slots(self):
        """Get the total available slots."""
        return self._available_slots

    def get_issued_tickets(self):
        """Get all issued tickets."""
        return self._issued_tickets.values()

    def park(self, vehicle):
        """Park the given vehicle."""
        if not self._available_slots:
            raise NoAvailableSlot

        slot = self._get_nearest_available_slot()
        slot.mark_unavailable()
        self._available_slots -= 1

        ticket = Ticket(vehicle, slot)
        self._issued_tickets.update({slot.get_number(): ticket})

        return ticket

    def unpark(self, slot_number):
        """Unpark the vehicle on given slot number."""
        ticket = self._issued_tickets.pop(slot_number, None)

        if not ticket:
            raise InvalidSlotNumber

        ticket.get_slot().mark_available()
        self._available_slots += 1

        return ticket

    def filter_tickets_by_colour(self, color):
        """Filter the tickets by given color."""
        return [ticket for ticket in self._issued_tickets.values()
            if ticket.get_vehicle().get_color() == color]

    def find_ticket_by_registration_number(self, registration_number):
        """Find the ticket by given registration number."""
        return next((ticket for ticket in self._issued_tickets.values()
            if ticket.get_vehicle().get_registration_number() == registration_number), None)

    def _get_nearest_available_slot(self):
        """Get the nearest slot available."""
        return next((slot for slot in self._slots if slot.is_available()), None)
