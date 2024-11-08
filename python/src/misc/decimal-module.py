from decimal import Decimal, getcontext
getcontext().prec = 11
f = Decimal(13/7)
print(f)


