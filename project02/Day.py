class Day:
	def __init__(self, date, cumulativeCases):
		self.__date: str = date
		self.__cumulativeCases: int = cumulativeCases
		__newDailyCases: int = None
		self.__sevenDayAverageCases: float = 0

	def getCumulativeCases(self):
		return self.__cumulativeCases

	def setNewDailyCases(self, newDailyCases):
		self.__newDailyCases = newDailyCases

	def getNewDailyCases(self):
		return self.__newDailyCases

	def setSevenDayAverageCases(self, sevenDayAverageCases):
		self.__sevenDayAverageCases = sevenDayAverageCases

	def getSevenDayAverageCases(self):
		return self.__sevenDayAverageCases

	def writeData(self, fpath):
		file = open(fpath, "a")
		file.write(self.__date + "," + str(self.__cumulativeCases) + "," + str(self.__sevenDayAverageCases) + "\n")
