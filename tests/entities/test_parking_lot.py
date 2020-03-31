from unittest import TestCase

from parking_lot.entities.parking_lot import ParkingLot


class TestParkingLot(TestCase):
    """Test the parking lot class."""

    def test_create_parking_lot(self):
        total_slots = 2

        parking_lot = ParkingLot(total_slots)

        self.assertEqual(parking_lot.get_total_slots(), total_slots)
        self.assertEqual(parking_lot.get_available_slots(), total_slots)
