# Iris Canavan, Section 3

from paydeductions import *

def main():
    print('Welcome to the net paycheck calculator')
    gross_pay = float(input("Enter gross pay: "))
    deductions, net_pay = deduct_net_pay(gross_pay)
    print('Gross pay = ${}'.format(round(gross_pay,2)))
    print('Deductions = ${}'.format(round(deductions,2)))
    print('Net pay = ${}'.format(round(net_pay,2)))

def deduct_net_pay(gross_pay):
    deductions = fed_tax(gross_pay) + state_tax(gross_pay) + ss_tax(gross_pay)
    net_pay = gross_pay - deductions
    return deductions, net_pay

main()
