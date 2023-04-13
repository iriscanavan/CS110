import csv
import matplotlib.pyplot as plt

FILE_PATH_OUTPUT = "covid-SF.csv"

def plot_SF_covid(fpath, date, seven_day_average):
	with open(fpath, mode = "r") as file:
		data_file = csv.reader(file)
		yearly_daily_data = []
		for line in data_file:
			date.append(line[0])
			seven_day_average.append(line[2])

def main():
	date = [] # x axis
	seven_day_average = [] # y axis
	plot_SF_covid(FILE_PATH_OUTPUT, date, seven_day_average)

	ax = plt.axes()
	ax.xaxis.set_major_locator(plt.MaxNLocator(4))
	ax.yaxis.set_major_locator(plt.MaxNLocator(4))
	plt.scatter(date, seven_day_average, c = "blue")
	plt.show()

main()
