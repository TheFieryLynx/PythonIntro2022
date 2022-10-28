#!/usr/bin/env python3

def maxfun(*args):
	s = args[0]
	num = 0
	sMax = -inf
	for i, f in enumerate(args[1:]):
		summ = 0
		for j in s:
			summ += f(j)
		if summ >= sMax:
			sMax = summ
			num = i
	return args[num + 1]

			

		