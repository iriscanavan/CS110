# Iris Canavan, Section 3

from paydeductions import *

def main():
    print('Welcome to the net paycheck calculator')
    grossPay = float(input("Enter gross pay: "))
    deductions, netPay = fDeductNetpay(grossPay)
    print('Gross pay = ${}'.format(round(grossPay,2)))
    print('Deductions = ${}'.format(round(deductions,2)))
    print('Net pay = ${}'.format(round(netPay,2)))

def fDeductNetpay(grossPay):
    deductions = fFedTax(grossPay) + fStateTax(grossPay) + fSSTax(grossPay)
    netPay = grossPay - deductions
    return deductions, netPay

main()
