# Iris Canavan, Section 3

HOTDOGS = 10
BUNS = 8

numAttend = int(input("How many people are attending the cookout? = "))
numHotdogs = int(input("How many hot dogs per person? = "))
Total = numAttend * numHotdogs

# minimum hotdog packages
minHotdogs = Total // HOTDOGS
if Total % HOTDOGS > 0:
	minHotdogs = minHotdogs + 1

# minimum bun packages
minBuns = Total // BUNS
if Total % BUNS > 0:
	minBuns = minBuns + 1

# hotdog remainder
minHotdogs = Total // HOTDOGS
if Total % HOTDOGS > 0:
	minHotdogs = minHotdogs + 1
remHotdogs = (HOTDOGS * minHotdogs - Total)

# hotdog bun remainder
minBuns = Total // BUNS
if Total % BUNS > 0:
	minBuns = minBuns + 1
remBuns = (BUNS * minBuns - Total)

print("The minimum number of packages of hot dogs required = ", minHotdogs)
print("The minimum number of packages of hot dog buns required = ", minBuns)
print("The number of hot dogs left over = ", remHotdogs)
print("The number of hot dog buns left over = ", remBuns)
