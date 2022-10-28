#!/usr/bin/env python3

from decimal import Decimal, getcontext

def run(f, x):
	return eval(f)

inp_func = input()
inp_num = int(input())

getcontext().prec = inp_num + 2

l = Decimal('-1.5')
r = Decimal('1.5')

prev = r - l + 1

while prev != r - l and r - l > 10 ** (-(inp_num + 1)):
	avg = (r + l) / 2
	avg_val = run(inp_func, avg)
	prev = r - l
	if avg_val > 0:
		r = avg 
	else:
		l = avg

print('{:.{prec}f}'.format(r, prec=inp_num))