#!/usr/bin/env python3

#ax^2+bx+c=0

import math

a, b, c = map(int, input().split(','))

if a == 0:	# bx+c = 0		
	if b != 0: 
		if c == 0:
			print(-1)
			exit(0)
		else:
			print(-c / b)
			exit(0)
	else:
		if c == 0:
			print(-1)
		else:
			print(0)
	exit(0)

D = b ** 2 - 4 * a * c

if D > 0:
	x1 = (-b + math.sqrt(D)) / (2 * a)
	x2 = (-b - math.sqrt(D)) / (2 * a)
	if x1 < x2:
		print(x1, x2)
	else:
		print(x2, x1)
elif D == 0:
	x = -b / (2 * a)
	print(x)
else:
	print(0)