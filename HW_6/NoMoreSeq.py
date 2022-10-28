#!/usr/bin/env python3

def nomore(seq):
	for i in range(len(seq)):
		for j in seq:
			if j <= seq[i]:
				yield j

#print(*nomore([n % 13 for n in range(5,23,3)]))