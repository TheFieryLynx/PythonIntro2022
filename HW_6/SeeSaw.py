#!/usr/bin/env python3

from itertools import tee, zip_longest, filterfalse

def seesaw(seq):
	it1, it2 = tee(seq, 2)
	for i in zip_longest(filter(lambda x: not x % 2, it1), filter(lambda x: x % 2, it2), fillvalue=None):
		for j in i:
			if j != None:
				yield j
		
