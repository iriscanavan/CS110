class Day:
	__date = None
	__cumulativeCases = None

	def __init__(self, date, cumulativeCases):
		self.__date = date
		self.__cumulativeCases = cumulativeCases

	def writeData(self, fpath):
		file = open(fpath, "a")
		file.write(self.__date + "," + self.__cumulativeCases + "\n")
