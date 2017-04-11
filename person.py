class Person:
    def __init__(self, name):
        self.name = name

class Staff(Person):

    employee_type = "Staff"

    def __init__(self, name):
        super(Staff, self).__init__(name)



class Fellow(Person):

    employee_type = "Fellow"

    def __init__(self, name):
        super(Fellow, self).__init__(name)
