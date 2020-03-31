from unittest import TestCase

from parking_lot.parking_manager import ParkingManager


class TestParkingManager(TestCase):
    """Test the parking manageer."""

    def setUp(self):
        self.manager = ParkingManager()

    def test_create_parking_lot(self):
        total_slots = 6

        output = self.manager.create_parking_lot(total_slots)

        self.assertEqual(f'Created a parking lot with {total_slots} slots', output)

    def test_parking(self):
        self.manager.create_parking_lot(2)

        output = self.manager.park('KA-01-HH-1234', 'White')

        self.assertEqual('Allocated slot number: 1', output)

    def test_no_available_slot_for_parking(self):
        self.manager.create_parking_lot(1)

        self.manager.park('KA-01-HH-1234', 'White')
        output = self.manager.park('KA-01-P-3333', 'White')

        self.assertEqual('Sorry, parking lot is full', output)

    def test_leaving_parking_lot(self):
        self.manager.create_parking_lot(2)
        self.manager.park('KA-01-HH-1234', 'White')
        self.manager.park('KA-01-P-3333', 'White')

        slot_number = 2
        output = self.manager.leave(slot_number)

        self.assertEqual(f'Slot number {slot_number} is free', output)
