from datetime import datetime as dt

str_date_time = "2019-08-03 16:23:40.8370"

str_date = str_date_time[ : str_date_time.find(" ") : ]
obj_date = dt.fromisoformat(str_date)
print("Date:", obj_date)
obj_date = dt.strptime(str_date_time, "%Y-%m-%d %H:%M:%S.%f")

print("Date:", obj_date.strftime("%m/%d/%y"))
print("24 hour time", obj_date.strftime("%H:%M:%S"))
print("12 hour time", obj_date.strftime("%I:%M:%S %p\n"))
print('----Using isocalendar----')
print("Isocalendar:", obj_date.isocalendar(), "\n")
print('----Using properties----')
print("Year:", obj_date.year)
print("Month:", obj_date.month)
print("Day:", obj_date.day, "\n")
print('----Using weekday function----')
print("Weekday:", obj_date.weekday())
