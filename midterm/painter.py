# Iris Canavan, Section 3

GALLONS_PAINT = 1 / 112
HOURS_LABOR = 8 / 112
PRICE_PER_HOUR = 35.00

def main():
	square_feet = float(input("Enter the square feet of wall to be painted: "))
	price_paint = float(input("Enter the price of the paint per gallon: "))

	gallons = fgallons_required(square_feet)
	hours = fhours_required(square_feet)
	paint_cost = fpaint_cost(price_paint, gallons)
	labor_cost = flabor_cost(hours)
	total_cost = ftotal_cost(paint_cost, labor_cost)

	print("-----Summary of painting charges----------------------")
	print("     You will need", format(gallons, '.2f'), "gallons of paint")
	print("     You will need", format(hours, '.2f'), "hours of labor")
	print("     The cost of paint is $", format(paint_cost, '.2f'))
	print("     The cost of labor is $", format(labor_cost, '.2f'))
	print("     Your total charges are $", format(total_cost, '.2f'))

def fgallons_required(square_feet):
	return square_feet * GALLONS_PAINT

def fhours_required(square_feet):
	return square_feet * HOURS_LABOR

def fpaint_cost(price_paint, gallons):
	return price_paint * gallons

def flabor_cost(hours):
	return hours * PRICE_PER_HOUR

def ftotal_cost(paint_cost, labor_cost):
	return labor_cost + paint_cost

main()
