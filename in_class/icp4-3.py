# Iris Canavan, Section 3

INITIAL_SALARY = 0.01

today_sal = INITIAL_SALARY
total = 0
days = int(input("How many days will you work for pennies a day? "))

for x in range(1,days + 1):
	 print("Salary on day", x, " = $", today_sal)
	 total = today_sal + total
	 today_sal = today_sal * 2

print("Total amount earned in 10 days = ", total)
