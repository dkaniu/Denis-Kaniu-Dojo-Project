from person import Person

class Room:
    add_people = []
    room_count = []
    avlble_space = 0

    def __init__(self):
        pass

    def create_room(self,name,type):
        self.name = name
        self.type=type
        Room.room_count.append(name)

        print("An office called {} has been successfully created!".format(name))

    def add_person(self, person_name, emp_type):
        self.emp_type = emp_type
        self.person = Person(person_name, emp_type, choice='Y')
        Room.add_people.append(person_name)
        print("{0} {1} has been successfully added! ".format(emp_type,person_name))





class LivingSpace(Room):
    def __init__(self):
        pass


class Office(Room):
    def __init__(self):
        pass





a = Room()
a.create_room('blue', 'office')
a.add_person('waithira', 'staff')
