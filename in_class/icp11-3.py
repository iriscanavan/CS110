# Iris Canavan, Section 3

def read_file():
	file = open("WorldSeriesWinners.txt", "r")
	return file.readlines()
	file.close()

def create_dictionary(WSW):
	num_times_WSW = {}
	for line in WSW:
		line = line.strip('\n')
		if line == "World Series Not Played in 1904" or line == "World Series Not Played in 1994":
			continue
		if line not in num_times_WSW:
			num_times_WSW[line] = 1
		else:
			num_times_WSW[line] += 1
	return num_times_WSW

def main():
	lst_WSW = read_file()
	dct_WSW = create_dictionary(lst_WSW)
	print("Team".ljust(30) + "Num of wins".rjust(15))
	for team, wins in dct_WSW.items():
		team_padding = 34 - len(team)
		print(team + "-" * team_padding + str(wins))

main()
