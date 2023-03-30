# Iris Canavan, Section 3

def main():
	sentence = input("Enter a sentence: ")
	list_count = fcount_letters(sentence)
	print("The sentence: ", sentence, "\n" "contains the following: \n Uppercase letters = ", list_count[0], "\n", "Lowercase letters = ", list_count[1], "\n", "Space = ", list_count[2])


def fcount_letters(pSentence):
	count_upper = 0
	count_lower = 0
	count_space = 0
	for char in pSentence:
		if char.isupper():
			count_upper += 1
		elif char.islower():
			count_lower += 1
		elif char.isspace():
			count_space += 1
	return [count_upper, count_lower, count_space]

main()
