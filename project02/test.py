import sys #debug

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

	for i in range(len(daily_data)):
		daily_data[i].writeData()

main()
