class Day:
	__date: int
	__cumulativeCases: int
	__newDailyCases: int

	def __init__(self, date, cumulativeCases):
		self.__date = date
		self.__cumulativeCases = cumulativeCases

	def getCumulativeCases(self):
		return int(self.__cumulativeCases)

	def setNewDailyCases(self, newDailyCases):
		self.__newDailyCases = newDailyCases

	def getNewDailyCases(self):
		return int(self.__newDailyCases)

	def writeData(self, fpath):
		file = open(fpath, "a")
		file.write(self.__date + "," + self.__cumulativeCases + "\n")
