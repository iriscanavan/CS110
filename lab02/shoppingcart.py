# Iris Canavan, Section 3

from math import trunc

PRICE_RASPBERRIES = 1.75
PRICE_STRAWBERRIES = 1.25
PRICE_APPLE = 0.5
PRICE_MANGO = 1.75

lbs_rasp = float(input("Please enter how many pounds of raspberries you would" +
		       " like to buy ($" + str(PRICE_RASPBERRIES) + "/lb): "))
lbs_straw = float(input("Please enter how many pounds of strawberries you" +
			" would like to buy ($" +
			str(PRICE_STRAWBERRIES) + "/lb): "))
lbs_apple = float(input("Please enter how many apples you would like to buy" +
			" ($" + str(PRICE_APPLE) + " each): "))
lbs_mango = float(input("Please enter how many mangoes you would like to buy" +
			" ($" + str(PRICE_MANGO) + " each): "))
customer_price = float(input("How much will you pay for the fruit? $"))

cost_rasp = lbs_rasp * PRICE_RASPBERRIES
cost_straw = lbs_straw * PRICE_STRAWBERRIES
cost_apple = lbs_apple * PRICE_APPLE
cost_mango = lbs_mango * PRICE_MANGO
store_total = cost_rasp + cost_straw + cost_apple + cost_mango

print("Total owed: $" + str(round(store_total, 2)))

# check customer payment
add_money = 0
while customer_price < store_total:
	print("Not enough money paid.")
	add_money = float(input("Enter more money = "))
	customer_price += add_money

change = customer_price - store_total
print("Change due: $" + str(change) + "\n")

# bills
BILL_FIVE_VALUE = 5;
BILL_ONE_VALUE = 1;
BILL_QUARTER_VALUE = 0.25;
BILL_DIME_VALUE = 0.1;
BILL_NICKEL_VALUE = 0.05;
BILL_PENNY_VALUE = 0.01;

bill_five_quant = trunc(change / BILL_FIVE_VALUE)
change -= bill_five_quant * BILL_FIVE_VALUE

bill_one_quant = trunc(change / BILL_ONE_VALUE)
change -= bill_one_quant * BILL_ONE_VALUE

bill_quarter_quant = trunc(change / BILL_QUARTER_VALUE)
change -= bill_quarter_quant * BILL_QUARTER_VALUE

bill_dime_quant = trunc(change / BILL_DIME_VALUE)
change -= bill_dime_quant * BILL_DIME_VALUE

bill_nickel_quant = trunc(change / BILL_NICKEL_VALUE)
change -= bill_nickel_quant * BILL_NICKEL_VALUE

bill_penny_quant = trunc(round(change / BILL_PENNY_VALUE))
change -= bill_penny_quant * BILL_PENNY_VALUE

print("Give the customer:")
if bill_five_quant != 0:
	print(str(bill_five_quant) + " $5 bill(s)")

if bill_one_quant != 0:
	print(str(bill_one_quant) + " $1 bill(s)")

if bill_quarter_quant != 0:
	print(str(bill_quarter_quant) + " quarter(s)")

if bill_dime_quant != 0:
	print(str(bill_dime_quant) + " dime(s)")

if bill_nickel_quant != 0:
	print(str(bill_nickel_quant) + " nickel(s)")

if bill_penny_quant != 0:
	print(str(bill_penny_quant) + " penny(pennies)")

print()
