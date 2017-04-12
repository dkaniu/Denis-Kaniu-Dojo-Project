import unittest
from room import Room

class TestRoomClass(unittest.TestCase):

    def test_create_room_successfully(self):
        inst = Room()
        inst.create_room('room', 'office')
        self.assertTrue(inst)


if __name__ == '__main__':
    unittest.main()
