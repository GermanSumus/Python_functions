from decimal import *

def dec(cash_value):
    cash_dec = Decimal(cash_value).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)
    return cash_dec
