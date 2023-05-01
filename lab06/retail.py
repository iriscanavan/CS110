# Iris Canavan, Section 3

from RetailClass import RetailItem

def main():
	list_retail = populate_data()
	print()
	print("------ Initial Data ------")
	print_data(list_retail)
	update_data(list_retail)
	print("---- Updated Inventory Data ----")
	print_data(list_retail)

def populate_data():
	list_data = [["Jacket", 12, "$59.95\n"],
		     ["Jeans", 40, "$34.95\n"],
		     ["Shirt", 20, "$24.95\n"]]
	list_objects = []
	for item in list_data:
		obj = RetailItem(item[0], item[1], item[2])
		list_objects.append(obj)
	return list_objects

def print_data(list_retail):
	for item in list_retail:
		print(item.__str__())
	print()

def update_data(list_retail):
	for item in list_retail:
		if item.get_description() == "Jacket":
			item.set_inventory(item.get_inventory() + 20)
		elif item.get_description() == "Jeans":
			item.set_inventory(item.get_inventory() -5)
		elif item.get_description() == "Shirt":
			item.set_inventory(item.get_inventory() + 35)

main()
