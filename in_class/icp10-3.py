# Iris Canavan, Section 3

def main():
	sentence = input("Enter a sentence: ")
	list_count = count_letters(sentence)
	print("The sentence:", sentence, "\n" "contains the following: \nUppercase letters = ", list_count[0], "\nLowercase letters = ", list_count[1], "\nSpace = ", list_count[2])


def count_letters(sentence):
	count_upper = 0
	count_lower = 0
	count_space = 0
	for char in sentence:
		if char.isupper():
			count_upper += 1
		elif char.islower():
			count_lower += 1
		elif char.isspace():
			count_space += 1
	return [count_upper, count_lower, count_space]

main()
