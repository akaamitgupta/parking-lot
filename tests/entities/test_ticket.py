from unittest import TestCase

from parking_lot.entities.slot import Slot
from parking_lot.entities.ticket import Ticket
from parking_lot.entities.vehicle import Vehicle


class TestTicket(TestCase):
    """Test the ticket class."""

    def test_create_ticket(self):
        vehicle = Vehicle('KA-01-HH-2701', 'Blue')
        slot = Slot(1)

        ticket = Ticket(vehicle, slot)

        self.assertEqual(ticket.get_vehicle(), vehicle)
        self.assertEqual(ticket.get_slot(), slot)
