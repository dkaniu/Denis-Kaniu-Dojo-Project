from unittest import TestCase
from room import Office

class TestCreateRoom(TestCase):
    def test_create_room(self):
        my_class_instance = Office()
        initial_room_count = len(my_class_instance.all_rooms)

        blue_office = my_class_instance.create_room('Blue', 'office')
        self.assertTrue(blue_office)

        new_room_count = len(my_class_instance.all_rooms)
        self.assertEqual(new_room_count - initial_room_count, 1)

