import csv

from Day import Day

FILE_PATH_INPUT = ["us-counties-2020.csv", "us-counties-2021.csv", "us-counties-2022.csv"]
FILE_PATH_OUTPUT = "covid-SF.csv"
WINDOW = 7

def read_input_file(fpath):
	with open(fpath, mode = "r") as file:
		data_file = csv.reader(file)
		yearly_daily_data = []
		for line in data_file:
			if (line[1] == "San Francisco"):
				yearly_daily_data.append(Day(line[0], line[4]))
		return yearly_daily_data


def main():
	daily_data = []
	for i in range(0, 3):
		daily_data += read_input_file(FILE_PATH_INPUT[i])

	# Calculate the new daily cases by subtracting yesterday's cumulative
	# cases from today's cumulative cases. The first day (daily_data[0])'s
	# new daily cases should always be the same as its cumulative cases.
	daily_data[0].setNewDailyCases(daily_data[0].getCumulativeCases())
	for i, value in enumerate(daily_data[1:], 1):
		daily_data[i].setNewDailyCases(daily_data[i].getCumulativeCases() - daily_data[i - 1].getCumulativeCases())

	for i in range(len(daily_data)):
		daily_data[i].writeData(FILE_PATH_OUTPUT)

main()
