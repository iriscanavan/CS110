# Iris Canavan, Section 3

from os import system, name
import sys
import csv
import pets

def read_data():
	pets_list = []
	with open("pets.csv", "r") as file:
		line_reader = csv.reader(file)
		for line in line_reader:
			if line[0] == "Dog":
				pets_list.append(pets.Dog(line[1], line[2], line[3], line[4]))
			elif line[0] == "Cat":
				pets_list.append(pets.Cat(line[1], line[2], line[3], line[4]))
			elif line[0] == "Fish":
				pets_list.append(pets.Fish(line[1], line[2], line[3], line[4]))
			elif line[0] == "Bird":
				pets_list.append(pets.Bird(line[1], line[2], line[3], line[4]))

	return pets_list

def display_pet_names(pets_list):
	print("-" * 10, "Show Pet Names", "-" * 10)
	for pet in pets_list:
		print(pet.get_name())
	print()

def search_pet(pets_list):
	print("-" * 10, "Search Pet", "-" * 10)
	search_name = input("What is the name of the pet you want to find? ")
	for i in range(len(pets_list)):
		if search_name == pets_list[i].get_name():
			print("%s\nindex: %d\n" % (pets_list[i], i))
			return
	print("Sorry, test is not in the list.\n")

def show_pets(pets_list):
	print("-" * 10, "Show Pets", "-" * 10)
	for lines in pets_list:
		print(lines.__str__())
	print()

def show_pet_type(pets_list):
	print("-" * 10, "Show Pet Type", "-" * 10)
	choose_type = input("What kind of pet would you like to find?\n" \
			    "Please enter a number between 1-4.\n" \
			    "1 = dog, 2 = cat, 3 = fish, 4 = bird ")
	for lines in pets_list:
		if choose_type == "1" and isinstance(lines, pets.Dog):
			print(lines)
		elif choose_type == "2" and isinstance(lines, pets.Cat):
			print(lines)
		elif choose_type == "3" and isinstance(lines, pets.Fish):
			print(lines)
		elif choose_type == "4" and isinstance(lines, pets.Bird):
			print(lines)
	print()

def sort_pet_names(pets_list):
	print("-" * 10, "Show Sorted Pet Names", "-" * 10)
	pets_list_sorted = sorted(pets_list, key = lambda pet: pet.get_name())
	for pet in pets_list_sorted:
		print(pet)
	print()

def show_menu(pets_list):
	print("-" * 10, "Pet Finder Menu", "-" * 10)
	print("1. Show Pet Names")
	print("2. Search for Pet")
	print("3. Show List")
	print("4. Shows Pets of Certain Type")
	print("5. Sort all the pets alphabetically")
	print("6. Exit the Program")
	print("-" * 37)

	choose_option = input("Please enter one of the above options: ")
	system("clear")

	if choose_option == "1":
		display_pet_names(pets_list)
	elif choose_option == "2":
		search_pet(pets_list)
	elif choose_option == "3":
		show_pets(pets_list)
	elif choose_option == "4":
		show_pet_type(pets_list)
	elif choose_option == "5":
		sort_pet_names(pets_list)
	elif choose_option == "6":
		sys.exit(0)
	else:
		print("Invalid choice")

def main():
	pets_list = read_data()
	while True:
		show_menu(pets_list)

main()
