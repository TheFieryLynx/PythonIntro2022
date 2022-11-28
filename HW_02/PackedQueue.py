#!/usr/bin/env python3

inp = eval(input())

lst = list()
lst_end = 0

for i in inp:
	if type(i) is tuple:
		a = list(i)
		a.reverse()
		lst = a + lst
	else:
		if i > 0:
			if i > len(lst):
				exit(0)
			t = tuple()
			p = lst[-i:]
			p.reverse()
			print(tuple(p))
			lst = lst[:-i]
		else:
			print(tuple())

