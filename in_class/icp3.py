# Iris Canavan, Section 3
year = int(input("Please enter a year = "))
if year % 100 == 0:
	if year % 400 == 0: 
        		print("Year ", year, "is a leap year")
	else:
			print("Year ", year, "is not a leap year")
elif year % 4 == 0:
	print("Year ", year, "is a leap year")	
else: 
	print("Year ", year, "is not a leap year")
