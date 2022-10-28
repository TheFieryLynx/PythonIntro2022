#!/usr/bin/env python3

from itertools import tee, zip_longest

def seesaw(seq):
	it1, it2 = tee(seq, 2)
	for i, j in enumerate(zip_longest(it1, it2, fillvalue='_')):
		print(i, j)
		if i % 2:
			yield j[1]
		else:
			yield j[0]
		
		
print(*seesaw(i//3 for i in range(1, 27, 2)))