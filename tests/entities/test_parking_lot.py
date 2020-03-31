from unittest import TestCase

from parking_lot.entities.vehicle import Vehicle
from parking_lot.entities.parking_lot import ParkingLot


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

        self.parking_lot.park(vehicle)

        self.assertEqual(parking_lot.get_available_slots(), self.total_slots - 1)

    def test_unpark_vehicle(self):
        vehicle = Vehicle('KA-01-HH-2701', 'Blue')

        ticket = self.parking_lot.park(vehicle)
        self.parking_lot.unpark(ticket.get_slot().get_number())

        self.assertEqual(parking_lot.get_available_slots(), self.total_slots)
