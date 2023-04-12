# Iris Canavan, Section 3

def fread_file():
	file = open("WorldSeriesWinners.txt", "r")
	return file.readlines()
	file.close()

def fcreate_dictionary(pWSW):
	num_times_WSW = {}
	for line in pWSW:
		line = line.strip('\n')
		if line == "World Series Not Played in 1904" or line == "World Series Not Played in 1994":
			continue
		if line not in num_times_WSW:
			num_times_WSW[line] = 1
		else:
			num_times_WSW[line] += 1
	return num_times_WSW

def main():
	lst_WSW = fread_file()
	dct_WSW = fcreate_dictionary(lst_WSW)
	print("Team						Num of Wins")
	for team, wins in dct_WSW.items():
		print(team, "-" * 30, wins,)

main()
