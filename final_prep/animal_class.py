class Animal():
	def __init__(self, name, age):
		self.__name = name
		self.__age = age

	def set_age(self, age):
		self.__age = age

	def __str__(self):
		return "My name is " + self.__name + " and I am " + str(self.__age) + " years old"

class Dog(Animal):
	def __init__(self, name, age, breed):
		super().__init__(name, age)
		self.__type = "dog"
		self.__breed = breed

	def get_type(self):
		return self.__type

	def __str__(self):
		str_output = (super().__str__() + "\n" + "I am a " + self.__type + " and my breed is " + self.__breed)
		return str_output
