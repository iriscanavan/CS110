class service_quote:
	def __init__(self, tax_rate):
		self.__tax_rate = tax_rate
		self.__parts_charges = 0
		self.__labor_charges = 0

	def get_parts_charges(self):
		return self.__parts_charges

	def get_labor_charges(self):
		return self.__labor_charges

	def get_parts_tax(self):
		return float(self.__parts_charges) * float(self.__tax_rate)

	def get_total_charges(self):
		return float(self.__parts_charges) + float(self.__labor_charges) + self.get_parts_tax()

	def set_parts_charges(self, pCharge):
		self.__parts_charges = pCharge

	def set_labor_charges(self, lCharge):
		self.__labor_charges = lCharge
