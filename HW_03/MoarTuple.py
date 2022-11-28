#!/usr/bin/env python3

def moar(a, b, n):
	cnt_a = 0
	cnt_b = 0
	for i in a:
		if i % n == 0:
			cnt_a = cnt_a + 1
	for i in b:
		if i % n == 0:
			cnt_b = cnt_b + 1
	return cnt_a > cnt_b
	