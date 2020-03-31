import pytest
from unittest import TestCase

from parking_lot.parking_manager import ParkingManager
from parking_lot.exceptions.parking_lot_not_found import ParkingLotNotFound


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

    def test_parking_lot_status(self):
        self.manager.create_parking_lot(2)

        registration_number = 'KA-01-HH-9898'
        colour = 'White'

        self.manager.park(registration_number, colour)
        self.manager.park('KA-01-HH-8989', 'White')
        self.manager.leave(2)

        output = self.manager.status()

        self.assertListEqual([
            ['Slot No.', 'Registration No', 'Colour'],
            ['1', registration_number, colour]
        ], output)

    def test_registration_numbers_for_cars_with_given_colour(self):
        self.manager.create_parking_lot(3)

        self.manager.park('KA-01-HH-1234', 'White')
        self.manager.park('KA-01-HH-8989', 'Blue')
        self.manager.park('KA-01-P-3333', 'White')

        output = self.manager.registration_numbers_for_cars_with_colour('White')

        self.assertEqual('KA-01-HH-1234, KA-01-P-3333', output)

    def test_registration_numbers_not_found_for_cars_with_given_colour(self):
        self.manager.create_parking_lot(3)

        self.manager.park('KA-01-HH-1234', 'White')
        self.manager.park('KA-01-HH-8989', 'Blue')
        self.manager.park('KA-01-P-3333', 'White')

        self.manager.leave(2)

        output = self.manager.registration_numbers_for_cars_with_colour('Blue')

        self.assertEqual('Not found', output)

    def test_slot_numbers_for_cars_with_given_colour(self):
        self.manager.create_parking_lot(3)

        self.manager.park('KA-01-HH-1234', 'White')
        self.manager.park('KA-01-HH-8989', 'Blue')
        self.manager.park('KA-01-P-3333', 'White')

        output = self.manager.slot_numbers_for_cars_with_colour('White')

        self.assertEqual('1, 3', output)

    def test_slot_numbers_not_found_for_cars_with_given_colour(self):
        self.manager.create_parking_lot(3)

        self.manager.park('KA-01-HH-1234', 'White')
        self.manager.park('KA-01-HH-8989', 'Blue')

        self.manager.leave(2)

        output = self.manager.slot_numbers_for_cars_with_colour('Blue')

        self.assertEqual('Not found', output)

    def test_slot_number_for_given_registration_number(self):
        self.manager.create_parking_lot(3)

        self.manager.park('KA-01-HH-8989', 'Blue')

        output = self.manager.slot_number_for_registration_number('KA-01-HH-8989')

        self.assertEqual(1, output)

    def test_slot_number_not_found_for_given_registration_number(self):
        self.manager.create_parking_lot(3)

        self.manager.park('KA-01-HH-1234', 'White')
        self.manager.park('KA-01-HH-8989', 'Blue')

        self.manager.leave(2)

        output = self.manager.slot_number_for_registration_number('KA-01-HH-8989')

        self.assertEqual('Not found', output)

    def test_no_parking_lot_found(self):
        with pytest.raises(ParkingLotNotFound):
            self.manager.park('KA-01-HH-1234', 'White')
