from room import Room

class Kitchen(Room):
	def __init__(self, name):
    		'''
			kitchen room inherited from the room class
			'''
		super().__init__(name)
		self.description = """\nYou are in the kitchen.\nYou can head west to the barracks and south to the dining area.\n"""
		self.contents = ["Medkit (3/3) uses left"]
		self.doors = {"w":"barracks", "s":"dining"}
		self.special = []
