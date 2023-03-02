FED_TAX = 0.1725
STATE_TAX = 0.0585
OASDI_TAX = 0.062
MEDICARE_TAX = 0.0145

def fFedTax(grossPay):
    return grossPay * FED_TAX

def fStateTax(grossPay):
    return grossPay * STATE_TAX

def fSSTax(grossPay):
    return grossPay * (OASDI_TAX + MEDICARE_TAX)
