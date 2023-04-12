class Day:
	def __init__(self, date, cases):
		self.__date = date
		self.__cases = cases

	def writeData(self, fpath):
		file = open(fpath, "a")
		file.write(self.__date + "," + self.__cases + "\n")
