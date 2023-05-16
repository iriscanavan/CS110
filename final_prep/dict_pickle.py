import pickle

FILE_PATH = 'students.dat'

def main():
	students = load_students()
	choice = 1
	while choice != 0:
		print()
		try:
			choice = int(input("1- Add Student, 2 - Display Students, 0 - Exit "))
			if choice == 1:
				add_student(students)
			elif choice == 2:
				display_students(students)
			elif choice == 0:
				print("Exiting")
			else:
				print("Invalid Input, enter 0, 1, 2")
		except ValueError:
			print("Enter a number and not a character")
	save_students(students)

def display_students(pDictStudents):
	for key in pDictStudents.keys():
		print("Student:", key, "\tMajor:", pDictStudents[key])
	print("-" * 50)

def load_students():
	try:
		file_input = open(FILE_PATH, "rb")
		dict_students = pickle.load(file_input)
		file_input.close()
	except IOError:
		dict_students = {}
	return dict_students

def add_student(pDictStudents):
	student = input('Enter student name: ')
	major = input('Enter major: ')
	if student not in pDictStudents:
		pDictStudents[student] = major
		print("Student", student, "has been added")
	else:
	 	print("Student", student, "already exists")

def save_students(pDictStudents):
	file_output = open(FILE_PATH, "wb")
	pickle.dump(pDictStudents, file_output)
	file_output.close()
	file_output.close()

main()
