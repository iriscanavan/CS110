FED_TAX = 0.1725
STATE_TAX = 0.0585
OASDI_TAX = 0.062
MEDICARE_TAX = 0.0145

def fed_tax(gross_pay):
    return gross_pay * FED_TAX

def state_tax(gross_pay):
    return gross_pay * STATE_TAX

def ss_tax(gross_pay):
    return gross_pay * (OASDI_TAX + MEDICARE_TAX)
