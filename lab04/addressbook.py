# Iris Canavan, Section 3

def main():
	menu()
	choice = menu_choice
	if choice == "1":
		print_address_book()
	elif choice == "2":
		search_contact()
	elif choice == "3":
		add_contact()
	elif choice == "4":
		delete_contact()
	elif choice == "5":
		again = input("Do you want to continue? (y/n): ")
		if again == "y":
			main()
		while again != "y" and again != "n":
			again = input("Do you want to continue? (y/n): ")

def menu():
	print("----MENU----------------------")
	print("    Print Address Book (1)")
	print("    Search Contact (2)")
	print("    Add New Contact (3)")
	print("    Delete Contact (4)")
	print("    Quit (5)")
	global menu_choice
	menu_choice = input("Enter your choice: ")
	while menu_choice != "1" and menu_choice != "2" and menu_choice != "3" and menu_choice != "4" and menu_choice != "5":
		print("Invalid input. Please try again.")
		menu_choice = input("Enter your choice: ")
	return menu_choice

def print_address_book():
	file = file_open("contacts.txt", "r")
	print(file.read())
	file.close()

def search_contact():
	search_contact = input("Name of contact you are searching for: ")
	file = file_open("contacts.txt", "r")
	line_number = 1
	boolFound = False
	for line in file:
		if line_number == 1:
			spaces = line.rstrip()
		elif line_number == 2:
			name = line.rstrip()
			if line.rstrip() == search_contact:
				boolFound = True
		elif line_number == 3:
			address = line.rstrip()
		elif line_number == 4:
			zipcode = line.rstrip()
			line_number = 0
		if boolFound and line_number == 0:
			print(spaces)
			print(name)
			print(address)
			print(zipcode)
			return
		line_number += 1
	file.close()
	if not boolFound:
		print(search_contact, "not found in address book")

def add_contact():
	name = input("Enter name: ")
	address = input("Enter street address: ")
	location = input("Enter city, state and zipcode: ")
	file = file_open("contacts.txt", "a")
	file.write("-" * 30)
	file.write("\n")
	file.write(name)
	file.write("\n")
	file.write(address)
	file.write("\n")
	file.write(location)
	file.write("\n")
	file.close()

def delete_contact():
	delete_contact = input("Name of contact you want to delete from the address book: ")
	file = file_open("contacts.txt", "r")
	directory = ""
	name = ""
	line_number = 1
	for line in file:
		if line_number == 1:
			dash_line = line
		elif line_number == 2:
			name = line
		elif line_number == 3:
			address = line
		elif line_number == 4:
			location = line
			line_number = 0
		if delete_contact != name.rstrip() and line_number == 0:
			directory += dash_line
			directory += name
			directory += address
			directory += location
		line_number += 1
	file.close()
	file = file_open("contacts.txt", "w")
	file.write(directory)
	file.close()

def file_open(fileName, mode):
	try:
		file_open = open("contacts.txt", mode)
		return file_open
	except FileNotFoundError:
		print("File not found")

main()
