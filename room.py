class Room:
    def __init__(self, name):
        self.room_nums = []
        self.name = name

    def room_type(self):
        return self


class Office(Room):
    number_of_people = 6

    def __init__(self, name):
        super(Office, self).__init__(name)



class LivingSpace(Room):

    number_of_people = 4

    def __init__(self, name):
        super(LivingSpace, self).__init__(name)
