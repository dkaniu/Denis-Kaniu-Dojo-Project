'''
This is the Persons model that initializes the Staff and Fellows.
'''
class Person:
    def __init__(self, name, emp_type, choice = 'Y' ):
        self.name = name
        self.emp_type = emp_type
        self.choice = choice

class Staff(Person):

    employee_type = "Staff"

    def __init__(self, name):
        super(Staff, self).__init__(name)



class Fellow(Person):

    employee_type = "Fellow"

    def __init__(self, name):
        super(Fellow, self).__init__(name)

