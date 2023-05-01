class Dog:
	def __init__(self, name, birthdate, breed, color):
		self.__name = name
		self.__birthdate = birthdate
		self.__breed = breed
		self.__color = color

	def get_name(self):
		return self.__name

	def set_name(self, name):
		self.__name = name

	def get_birthdate(self):
		return self.__birthdate

	def set_birthdate(self, birthdate):
		self.__birthdate = birthdate

	def get_breed(self):
		return self.__breed

	def set_breed(self, breed):
		self.__breed = breed

	def get_color(self):
		return self.__color

	def set_color(self, color):
		self.__color = color

	def __str__(self):
		return f"{self.__name} is a {self.__color} {self.__breed} born on {self.__birthdate}"

class Cat:
	def __init__(self, name, birthdate, breed, color):
		self.__name = name
		self.__birthdate = birthdate
		self.__breed = breed
		self.__color = color

	def get_name(self):
		return self.__name

	def set_name(self, name):
		self.__name = name

	def get_birthdate(self):
		return self.__birthdate

	def set_birthdate(self, birthdate):
		self.__birthdate = birthdate

	def get_breed(self):
		return self.__breed

	def set_breed(self, breed):
		self.__breed = breed

	def get_color(self):
		return self.__color

	def set_color(self, color):
		self.__color = color

	def __str__(self):
		return f"{self.__name} is a {self.__color} {self.__breed} born on {self.__birthdate}"

class Fish:
	def __init__(self, name, birthdate, fish_type, color):
		self.__name = name
		self.__birthdate = birthdate
		self.__fish_type = fish_type
		self.__color = color

	def get_name(self):
		return self.__name

	def set_name(self, name):
		self.__name = name

	def get_birthdate(self):
		return self.__birthdate

	def set_birthdate(self, birthdate):
		self.__birthdate = birthdate

	def get_breed(self):
		return self.__fish_type

	def set_breed(self, fish_type):
		self.__breed = fish_type

	def get_color(self):
		return self.__color

	def set_color(self, color):
		self.__color = color

	def __str__(self):
		return f"{self.__name} is an {self.__color} {self.__fish_type} born on {self.__birthdate}"

class Bird:
	def __init__ (self, name, birthdate, bird_type, color):
		self.__name = name
		self.__birthdate = birthdate
		self.__bird_type = bird_type
		self.__color = color

	def get_name(self):
		return self.__name

	def set_name(self, name):
		self.__name = name

	def get_birthdate(self):
		return self.__birthdate

	def set_birthdate(self, birthdate):
		self.__birthdate = birthdate

	def get_breed(self):
		return self.__bird_type

	def set_breed(self, fish_type):
		self.__breed = bird_type

	def get_color(self):
		return self.__color

	def set_color(self, color):
		self.__color = color

	def __str__(self):
		return f"{self.__name} is a {self.__color} {self.__bird_type} born on {self.__birthdate}"
