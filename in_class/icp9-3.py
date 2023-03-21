# Iris Canavan, Section 3

lst_cum_covid = [2, 5, 9, 22, 67, 123, 345, 654, 845, 1234, 3050, 6453]
lst_daily_cases = [lst_cum_covid[0]]
lst_mov_avg = [lst_daily_cases[0]]

for i in range(1, len(lst_cum_covid)):
	lst_daily_cases.append(lst_cum_covid[i] - lst_cum_covid[i - 1])

for i in range(1, len(lst_cum_covid)):
	lst_mov_avg.append(round(lst_cum_covid[i] / (i + 1), 2))

print("Cumulative Cases =", lst_cum_covid)
print("Daily Cases =", lst_daily_cases)
print("Moving Average =", lst_mov_avg)
