#!/usr/bin/env python3

a_1 = float("inf")
b_1 = float("inf")
c_1 = float("inf")

a_2 = float("-inf")
b_2 = float("-inf")
c_2 = float("-inf")

inp = input()
while inp != '':
	a, b, c = map(float, inp.split(','))

	if a < a_1:
		a_1 = a
	if a > a_2:
		a_2 = a
	
	if b < b_1:
		b_1 = b
	if b > b_2:
		b_2 = b
	
	if c < c_1:
		c_1 = c
	if c > c_2:
		c_2 = c
	
	inp = input()
	
print(abs(a_1 - a_2) * abs(b_1 - b_2) * abs(c_1 - c_2))
	