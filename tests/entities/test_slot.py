from unittest import TestCase

from parking_lot.entities.slot import Slot


class TestSlot(TestCase):
    """Test the slot class."""

    def test_create_slot(self):
        number = 1

        slot = Slot(number)

        self.assertEqual(slot.get_number(), number)
        self.assertEqual(slot.is_available(), True)

    def test_mark_unavailable(self):
        number = 1

        slot = Slot(number)
        slot.mark_unavailable()

        self.assertEqual(slot.is_available(), False)

    def test_mark_available(self):
        number = 1

        slot = Slot(number)
        slot.mark_unavailable()
        slot.mark_available()

        self.assertEqual(slot.is_available(), True)
