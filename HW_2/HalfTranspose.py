#!/usr/bin/env python3

first_line = input().split(',')

n = len(first_line)

matrix = list()
matrix.append(first_line)

for i in range(n - 1):
	matrix.append(input().split(','))

printLength = 2

print(matrix[0][0])

for i in range(1, n):
	strs = []
	for j in range(0, printLength):
		strs.append(matrix[i][j])
	for j in range(printLength - 2, -1, -1):
		strs.append(matrix[j][i])
	print(",".join(strs))
	printLength = printLength + 1
	

	