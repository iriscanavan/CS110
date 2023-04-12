# Iris Canavan, Section 3

from servicequote_class import service_quote as sq

def main():
	customer = input("Enter customer: ")
	make_model = input("Enter vehicle make and model: ")
	service = input("Enter service description ")
	tax_rate = float(input("Enter tax rate: "))

	service_quote = (sq(tax_rate))

	cont = "n"
	while cont == "n":
		parts = float(input("Enter cost of parts: "))
		labor = float(input("Enter cost of labor: "))

		service_quote.set_parts_charges(parts)
		service_quote.set_labor_charges(labor)

		print("CUSTOMER", "-" * 30)
		print("Customer: ", customer)
		print("Make/Model: ", make_model)
		print("Service Description: ", service)
		print("SERVICE", "-" * 30)
		print("Parts charges = $", parts)
		print("Labor charges = $", labor)
		print("Taxes = $", format(service_quote.get_parts_tax(), ".2f"))
		approve = input("Approve charges (y) or disapprove and re-enter (n): ")
		if approve == "y":
			break
		elif approve == "n":
			cont = "n"
		else:
			print("Invalid input")
	print("Total charges inclduing taxes: ", format(service_quote.get_total_charges(), ".2f"))

main()
