#!/usr/bin/env python3

from decimal import Decimal, getcontext
from math import factorial

getcontext().prec = 10000

def PiGen():
	k = -1
	s = 0
	num = Decimal(426880) * Decimal(10005).sqrt()
	
	while True:
		k += 1
		numerator = factorial(6 * k) * (545140134 * k + 13591409)
		denominator = factorial(3 * k) * factorial(k) ** 3 * (-262537412640768000) ** k
		s += Decimal(numerator) / Decimal(denominator)
		yield num / s
		

#for i, p in enumerate(PiGen()):
#	if i>120:
#		break
#print(str(p)[1400:1470])