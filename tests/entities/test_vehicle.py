from unittest import TestCase

from parking_lot.entities.vehicle import Vehicle


class TestVehicle(TestCase):
    """Test the vehicle class."""

    def test_create_vehicle(self):
        registration_number = 'KA-01-HH-2701'
        colour = 'Blue'

        vehicle = Vehicle(registration_number, colour)

        self.assertEqual(vehicle.get_registration_number(), registration_number)
        self.assertEqual(vehicle.get_colour(), colour)
