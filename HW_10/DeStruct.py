#!/usr/bin/env python3

import sys, base64

inp = input()
encoded = base64.b85decode(inp)

heading = []
heading_end = 0
record_size = 0

for i, v in enumerate(encoded):
	if hex(v) == hex(0):
		heading_end = i;
		break
	else:
		record_size += abs(int.from_bytes([v], byteorder='big', signed=True))
		heading.append(int.from_bytes([v], byteorder='big', signed=True))
#print(heading, record_size, len(encoded), heading_end)
res = 0
l = (len(encoded) - heading_end - 1) // record_size
#print(l)
for i in range(l):
	tmp = encoded[heading_end + 1 + i * record_size: heading_end + 1 + i * record_size + record_size]
	delta = 0
	for j in heading:
		if j < 0:
			res += int.from_bytes(tmp[delta:abs(j) + delta], byteorder='big', signed=True)
		else:
			res += int.from_bytes(tmp[delta:abs(j) + delta], byteorder='big', signed=False)
		delta += abs(j)
print(res)
