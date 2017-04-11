class Room:
	all_rooms = []
	def __init__(self):
		pass

class Office(Room):
	def __init__(self):
		pass

	def create_room(self, name, type):
		self.name = name
		self.type = type
		if type == 'office':
			super().all_rooms.append([1])
			return True
		else:
			return False

class LivingSpace(Room):

	def __init__(self):
		super().all_rooms.append([1])

	def create_room(self, name,type):
		self.name = name
		self.type = type

