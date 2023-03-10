# Iris Canavan, Section 3

import sys

file = ""
err = False

try:
	file = open("data.csv", "r")
except FileNotFoundError:
	err = True
else:
	print("Sums for each line:")
	line = ""
	for line in file:
		sum = 0
		for char in line.rstrip():
			if char != ",":
				sum += int(char)
		print(line.rstrip(), "=", sum)
finally:
	if file != "":
		file.close()

	if err:
		print("Program completed with errors\n")
		sys.exit(-1)
	else:
		file.close()
		print("\nProgram completed successfully without errors\n")
		sys.exit(0)
