class Day:
	__date: int
	__cumulativeCases: int
	__newDailyCases: int
	__sevenDayAverageCases: float

	def __init__(self, date, cumulativeCases):
		self.__date = date
		self.__cumulativeCases = cumulativeCases
		self.__sevenDayAverageCases = 0

	def getCumulativeCases(self):
		return int(self.__cumulativeCases)

	def setNewDailyCases(self, newDailyCases):
		self.__newDailyCases = newDailyCases

	def getNewDailyCases(self):
		return int(self.__newDailyCases)

	def setSevenDayAverageCases(self, sevenDayAverageCases):
		self.__sevenDayAverageCases = sevenDayAverageCases

	def getSevenDayAverageCases(self):
		return float(self.__sevenDayAverageCases)

	def writeData(self, fpath):
		file = open(fpath, "a")
		file.write(self.__date + "," + self.__cumulativeCases + "\n")
