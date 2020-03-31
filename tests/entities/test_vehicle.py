from unittest import TestCase

from parking_lot.entities.vehicle import Vehicle


class TestVehicle(TestCase):
    """Test the vehicle class."""

    def test_create_vehicle(self):
        registration_number = 'KA-01-HH-2701'
        color = 'Blue'

        vehicle = Vehicle(registration_number, color)

        self.assertEqual(vehicle.get_registration_number(), registration_number)
        self.assertEqual(vehicle.get_color(), color)
