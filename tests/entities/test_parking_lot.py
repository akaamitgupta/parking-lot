import pytest
from unittest import TestCase

from parking_lot.entities.vehicle import Vehicle
from parking_lot.entities.parking_lot import ParkingLot
from parking_lot.exceptions.no_available_slot import NoAvailableSlot


class TestParkingLot(TestCase):
    """Test the parking lot class."""

    def setUp(self):
        self.total_slots = 2
        self.parking_lot = ParkingLot(self.total_slots)

    def test_create_parking_lot(self):
        self.assertEqual(self.parking_lot.get_total_slots(), self.total_slots)
        self.assertEqual(self.parking_lot.get_available_slots(), self.total_slots)

    def test_park_vehicle(self):
        vehicle = Vehicle('KA-01-HH-2701', 'Blue')

        ticket = self.parking_lot.park(vehicle)

        self.assertEqual(self.parking_lot.get_available_slots(), self.total_slots - 1)
        self.assertEqual(ticket.get_slot().get_number(), 1)

    def test_unpark_vehicle(self):
        vehicle = Vehicle('KA-01-HH-2701', 'Blue')

        ticket = self.parking_lot.park(vehicle)
        ticket = self.parking_lot.unpark(ticket.get_slot().get_number())

        self.assertEqual(self.parking_lot.get_available_slots(), self.total_slots)
        self.assertEqual(ticket.get_slot().get_number(), 1)

    def test_park_vehicle_fail(self):
        vehicle1 = Vehicle('KA-01-HH-2701', 'Blue')
        vehicle2 = Vehicle('KA-01-HH-2702', 'Black')
        vehicle3 = Vehicle('KA-01-HH-2703', 'Brown')

        self.parking_lot.park(vehicle1)
        self.parking_lot.park(vehicle2)

        with pytest.raises(NoAvailableSlot):
            self.parking_lot.park(vehicle3)
