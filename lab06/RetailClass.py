class RetailItem:
	def __init__(self, description, inventory, price):
		self.__description = description
		self.__inventory = inventory
		self.__price = price

	def get_description(self):
		return self.__description

	def set_description(self, description):
		self.__descriptioin = description

	def get_inventory(self):
		return self.__inventory

	def set_inventory(self, inventory):
		self.__inventory = inventory

	def get_price(self):
		return self.__price

	def set_price(self, price):
		self.__price = price

	def __str__(self):
		return f"Description: {self.__description}\n Units in Inventory: {self.__inventory}\n Price: {self.__price}"
