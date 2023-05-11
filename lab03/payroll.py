# Iris Canavan, Section 3

hours_worked = 0
pay_rate = 0

def main():
	print("Welcome to the Payroll Manager!")
	print("-" * 90)
	salary = 40 * pay_rate
	sum_salary = 0
	sum_overtime_pay = 0
	salary, overtime_salary = fPayroll("Michael", 38.00, 18.34)
	sum_salary += salary
	sum_overtime_pay += overtime_salary
	salary, overtime_salary = fPayroll("Mary ", 45.50, 15.88)
	sum_salary += salary
	sum_overtime_pay += overtime_salary
	salary, overtime_salary = fPayroll("Nicole", 51.20, 22.45)
	sum_salary += salary
	sum_overtime_pay += overtime_salary
	salary, overtime_salary = fPayroll("Robert", 42.00, 21.34)
	sum_salary += salary
	sum_overtime_pay += overtime_salary
	salary, overtime_salary = fPayroll("Suzanne", 38.00, 19.21)
	sum_salary += salary
	sum_overtime_pay += overtime_salary
	print("-" * 90)
	print("Sum Regular Pay: $", format(sum_salary, '.2f'))
	print("Sum Overtime Pay: $", format(sum_overtime_pay, '.2f'))

def fPayroll(name, hours_worked, pay_rate):
	overtime_pay = pay_rate * 1.5
	overtime_salary = 0
	if hours_worked > 40.00:
		overtime_salary = (hours_worked - 40) * overtime_pay
		salary = 40 * pay_rate
	else:
		salary = hours_worked * pay_rate
		overtime_pay = 0
	print("Employee:", name, '\t', "Hours worked:", format(hours_worked,
		'.2f'), '\t', "Pay per hour: $", pay_rate, '\t', "Salary: $",
		format(overtime_salary + salary, '.2f'), '\t')
	return salary, overtime_salary

main()
