import unittest
from room import Person

class TestRoomClass(unittest.TestCase):

    def test_create_room_successfully(self):
        inst = Person('name', 'staff_or_fellow')
        self.assertTrue(inst)


if __name__ == '__main__':
    unittest.main()
