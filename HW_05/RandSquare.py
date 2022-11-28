#!/usr/bin/env python3

import math
import random

def randsquare(A, B):
	diag = math.hypot(A[0] - B[0], A[1] - B[1])
	a = diag / math.sqrt(2)
	x = random.uniform(0, a)
	y = random.uniform(0, a)
	# косинус угла A между диагональю и осью OY
	cosA = (A[0] - B[0]) / diag
	sinA = (A[1] - B[1]) / diag
	# нужно повернуть на угол B = 45 - A
	c = math.sqrt(2) / 2
	cosB = c * cosA + c * sinA
	sinB = c * cosA - c * sinA
	x1 = x * cosB + y * sinB
	y1 = - x * sinB + y * cosB
	return B[0] + x1, B[1] + y1