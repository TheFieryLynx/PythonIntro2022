#!/usr/bin/env python3

from fractions import Fraction
from decimal import Decimal

def add_frac(dig):
	return "Fraction('" + dig + "')"

def add_fracdec(dig):
	return "Fraction(Decimal('" + dig + "'))"

def add_number(dig):
	if '.' in dig:
		return add_fracdec(dig)
	return add_frac(dig)

symbols = '()+-/*%'

inp = input()
res_str = ''
dig = ''
for i in inp:
	if i in symbols:
		if dig != '':
			res_str += add_number(dig)
			dig = ''
		res_str += i
	
	if i.isdigit():
		dig += i
		
	if i == '.':
		dig += i
		
if dig != '':
	res_str += add_number(dig)

print(Fraction(eval(res_str)))