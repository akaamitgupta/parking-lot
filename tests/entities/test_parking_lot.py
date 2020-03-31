import pytest
from unittest import TestCase

from parking_lot.entities.vehicle import Vehicle
from parking_lot.entities.parking_lot import ParkingLot
from parking_lot.exceptions.no_available_slot import NoAvailableSlot
from parking_lot.exceptions.duplicate_vehicle import DuplicateVehicle
from parking_lot.exceptions.invalid_slot_number import InvalidSlotNumber


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

    def test_uppark_vehicle_fail(self):
        vehicle = Vehicle('KA-01-HH-2701', 'Blue')

        self.parking_lot.park(vehicle)

        with pytest.raises(InvalidSlotNumber):
            self.parking_lot.unpark(2)

    def test_filter_tickets_by_colour(self):
        vehicle = [
            {'registration_number': 'KA-01-HH-2701', 'colour': 'Blue' },
            {'registration_number': 'KA-01-HH-2702', 'colour': 'Black' },
        ]
        vehicle1 = Vehicle(vehicle[0]['registration_number'], vehicle[0]['colour'])
        vehicle2 = Vehicle(vehicle[1]['registration_number'], vehicle[1]['colour'])

        self.parking_lot.park(vehicle1)
        self.parking_lot.park(vehicle2)

        filtered_tickets = self.parking_lot.filter_tickets_by_colour(vehicle[0]['colour'])
        registration_numbers = [ticket.get_vehicle().get_registration_number() for ticket in filtered_tickets]

        self.assertEqual(registration_numbers, [vehicle[0]['registration_number']])

    def test_find_ticket_by_registration_number(self):
        vehicle = [
            {'registration_number': 'KA-01-HH-2701', 'colour': 'Blue' },
            {'registration_number': 'KA-01-HH-2702', 'colour': 'Black' },
        ]
        vehicle1 = Vehicle(vehicle[0]['registration_number'], vehicle[0]['colour'])
        vehicle2 = Vehicle(vehicle[1]['registration_number'], vehicle[1]['colour'])

        self.parking_lot.park(vehicle1)
        self.parking_lot.park(vehicle2)

        ticket = self.parking_lot.find_ticket_by_registration_number(vehicle[0]['registration_number'])

        self.assertEqual(ticket.get_vehicle().get_registration_number(), vehicle[0]['registration_number'])

    def test_find_ticket_by_registration_number_fail(self):
        vehicle = [
            {'registration_number': 'KA-01-HH-2701', 'colour': 'Blue' },
            {'registration_number': 'KA-01-HH-2702', 'colour': 'Black' },
        ]
        vehicle1 = Vehicle(vehicle[0]['registration_number'], vehicle[0]['colour'])
        vehicle2 = Vehicle(vehicle[1]['registration_number'], vehicle[1]['colour'])

        self.parking_lot.park(vehicle1)
        self.parking_lot.park(vehicle2)

        ticket = self.parking_lot.find_ticket_by_registration_number('KA-01-HH-2703')

        self.assertEqual(ticket, None)

    def test_duplicate_vehicle_parking(self):
        vehicle = Vehicle('KA-01-HH-2701', 'Blue')

        self.parking_lot.park(vehicle)

        with pytest.raises(DuplicateVehicle):
            self.parking_lot.park(vehicle)