# Iris Canavan, Section 3

def power(num, exp):
	if exp == 0:
		return 1
	else:
		return num * power(num, exp - 1)

def main():
	num1 = 5
	num2 = 3
	power(num1, num2)
	print("Num1 = ", num1, " / Num2 = ", num2 )
	print("The result = ", power(num1, num2))

main()
