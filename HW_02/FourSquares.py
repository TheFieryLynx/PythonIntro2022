#!/usr/bin/env python3

import math 

N = int(input())
x = 0
while x * x * 4 < N:
	x = x + 1
Y = x
while x * x <= N:
	while Y and (Y - 1) * (Y - 1) * 3 >= N - x * x:
		Y = Y - 1
	Z = Y
	y = Z
	while y <= x and x * x + y * y <= N:
		while Z and (Z - 1) * (Z - 1) * 2 >= N - x * x - y * y:
			Z = Z - 1
		t = Z
		z = t
		while z <= y and x * x + y * y + z * z <= N:
			while t * t > N - x * x - y * y - z * z:
				t = t - 1
			if x * x + y * y + z * z + t * t == N:
				print(x, y, z, t)
			z = z + 1
		y = y + 1
	x = x + 1
	


