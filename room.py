"""
Room Allocation System
Usage:
  room.py create_room <room_name> <room_type>...
  room.py add_person <person_name> <emp_type>...
  room.py print_room <room_name>
  room.py print_allocations [-o=filename]
  room.py print_unallocated [-o=filename]
  room.py reallocate_person <person_identifier> <new_room_name
  room.py load_people
  room.py save_state [--db=sqlite_database]
  room.py load_state <sqlite_database>
Options:
  -h --help     Show help info.
"""
from docopt import docopt
from person import Person


class Room:
    add_people = []
    room_names = []
    room_size = 0

    def __init__(self):
        pass

    def create_room(self, room_type, room_name):
        self.room_type = room_type
        self.room_name = room_name


        Room.room_names.append(room_name)
        if room_type == 'office':
            Room.room_size = 6
        elif room_type == 'livingspace':
            Room.room_size = 4
        else:
            Room.room_size = 0


        print("{} {} has been successfully created!".format( self.room_type, room_name))



    def add_person(self, person_name, emp_type):
        self.person_name = person_name
        self.emp_type = emp_type
        self.person = Person(person_name, emp_type, choice='Y')


        Room.add_people.append(self.person_name)
        print("{} {} has been successfully added! ".format(person_name, emp_type))


class LivingSpace(Room):
    def __init__(self):
        #initializes the LivingSpace sub class
        pass


class Office(Room):
    def __init__(self):
        #initializes the Office sub class
        pass



if __name__ == '__main__':
    arguments = docopt(__doc__, version='Denis-Kaniu-Dojo-Allocation v_0')
    Room().create_room(arguments['<room_type>'], arguments['<room_name>'])
    Room().add_person(arguments['<person_name>'], arguments['<emp_type>'])
