# Iris Canavan, Section 3

import pets

import csv

def read_data():
	pets_list = []
	with open("pets.csv", "r") as file:
		line_reader = csv.reader(file)
		for line in line_reader:
			if line == "Dog":
				pets_list.append(pets.Dog(line[1], line[2], line[3], line[4]))
			elif line == "Cat":
				pets_list.append(pets.Cat(line[1], line[2], line[3], line[4]))
			elif line == "Fish":
				pets_list.append(pets.Fish(line[1], line[2], line[3], line[4]))
			elif line == "Bird":
				pets_list.append(pets.Bird(line[1], line[2], line[3], line[4]))

	return pets_list

def display_pet_names(pets_list):
	print("--Show Pet Names-----------")
	for pet in pets_list:
		print(pet.get_name())

def search_pet(pets_list):
	print("--Search Pet---------------")
	search_name = input("What is the name of the pet you want to find? ")
	for i, pet in enumerate(pets_list):
		if pet.get_name() == search_name:
			found = True
			print("Name: ", pet[1], "Birthdate: ", pet[2], "Breed: ",  pet[3], "Color: ", pet[4])
			print("Index: ", i)
		if pet.get_name() != search_name:
			print("Pet not found in list")

def show_pets(pets_list):
	print("--Show Pets----------------")
	for pet in pets_list:
		print(pet)

def show_pet_type(pets_list):
	print("--Show Pet Type------------")
	choose_type = input("What kind of pet would you like to find? Please enter a number between 1-5. 1 = dog, 2 = cat, 3 = fish, 4 = bird ")
	legal_types = {"dog", "cat", "fish", "bird"}
	if choose_type not in legal_types:
		print("Invalid pet type")
	else:
		pets_of_type = [pet for pet in pets_list if
		type(pet).__name__.lower() == choose_type]
		if len(pets_of_type) == 0:
			print("No pets of that type in list")
		else:
			print(f"List of all {choose_type}s:")
			for pet in pets_of_type:
				print(pet)
def sort_pet_names(pets_list):
	print("--Show Sorted Pet Names-------")
	pets_list_sorted = sorted(pets_list, key = lambda pet: pet.get_name())
	for pet in pets_list_sorted:
		print(pet)

def show_menu():
	print("--------Pet Finder Menu------------")
	print("1. Show Pet Names")
	print("2. Search for Pet")
	print("3. Show List")
	print("4. Shows Pets of Certain Type")
	print("5. Sort all the pets alphabetically")
	print("6. Exit the Program")
	print("-----------------------------------")
	choose_option = input("Please enter one of the above options: ")

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

def main():
	pets_list = read_data()
	print(pets_list)
	show_menu()

main()
