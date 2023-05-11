from datetime import datetime as dt

def main():
	lst_data = read_file()
	print("Weekday count:", count_rentals(lst_data))

def read_file():
	lst_dates = []
	file = open("BikeRental.csv", "r")
	for line in file:
		lst_dates.append(line.split(",")[0])
	file.close()
	return lst_dates

def count_rentals(lst_data):
	lst_count = [0, 0, 0, 0, 0]
	bln_first = True
	for elt in lst_data:
		if not bln_first:
			str_date = elt[ :elt.find(" "): ]
			obj_date = dt.fromisoformat(str_date)
			int_weekday = obj_date.weekday()
			if int_weekday < 5:
				lst_count[int_weekday] += 1
		bln_first = False
	return lst_count

main()
