# Iris Canavan, Section 3

from datetime import datetime

FILE_PATH = "BikeRental.csv"

def read_file():
	lines = []
	fp = open(FILE_PATH, "r")
	for line in fp:
		lines.append(line.strip())
	return lines

def dist_rentals(pList):
	night = 0
	morning = 0
	afternoon = 0
	tpl = []

	for item in pList:
		starttime = datetime.strptime(item, "%Y-%m-%d %H:%M:%S.%f")
		hour = starttime.hour
		if hour >= 0 and hour < 6:
			night += 1
		elif hour >= 6 and hour < 12:
			morning += 1
		elif hour >= 12 and hour < 18:
			afternoon += 1
		else:
			print("invalid hour", hour)

	tpl.append(night)
	tpl.append(morning)
	tpl.append(afternoon)
	return tpl

def main():
	lst = read_file()
	tpl = dist_rentals(lst)
	print("-" * 70)
	print("Distribution of rentals over 24 hours")
	print("-" * 70)
	print("Percentage of night rentals: ", tpl[0])
	print("Percentage of morning rentals: ", tpl[1])
	print("Percentage of afternoon rentals: ", tpl[2])

main()
