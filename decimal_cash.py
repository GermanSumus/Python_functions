from decimal import *

def dec(cash_value):
    monetize = Decimal(cash_value).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)
    return monetize
