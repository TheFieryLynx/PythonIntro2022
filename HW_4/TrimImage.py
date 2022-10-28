#!/usr/bin/env python3

def print_matrix(matrix):
	for row in matrix:
		for elem in row:
			print(elem, end = '')
		print()

inp = input()
coords = list()
items = list()
minX = float("inf")
minY = float("inf")
maxX = float("-inf")
maxY = float("-inf")

while inp != '':
	parsed_input = inp.split()
	parsed_input_int = list(map(int, parsed_input[:-1]))
	if parsed_input_int[2] == 0 or parsed_input_int[3] == 0:
		inp = input()
		continue
#	print(parsed_input)
#	print(parsed_input_int)
	coords.append(parsed_input_int)
	items.append(parsed_input[-1])
	
#	print(coords)
#	print(items)
	minX = min(minX, parsed_input_int[0])
	minX = min(minX, parsed_input_int[0] + parsed_input_int[2])
	
	minY = min(minY, parsed_input_int[1])
	minY = min(minY, parsed_input_int[1] + parsed_input_int[3])
	
	maxX = max(maxX, parsed_input_int[0])
	maxX = max(maxX, parsed_input_int[0] + parsed_input_int[2])
	
	maxY = max(maxY, parsed_input_int[1])
	maxY = max(maxY, parsed_input_int[1] + parsed_input_int[3])
	
	inp = input()

#print(items, coords)
#print(minX, minY, maxX, maxY)

width = abs(minX - maxX)
length = abs(minY - maxY)

#print(width, length)

matrix = [['.'] * width for i in range(length)]

#print(items)
for i, elem in enumerate(items):
#	print("=============================")
#	print(elem, coords[i])
	deltaX = abs(minX - coords[i][0])
	deltaY = abs(minY - coords[i][1])
	l1 = deltaX
	l2 = deltaY
	r1 = l1 + coords[i][2]
	r2 = l2 + coords[i][3]
	if l1 > r1:
		l1, r1 = r1, l1
	if l2 > r2:
		l2, r2 = r2, l2
#	print(l1, r1)
#	print(l2, r2)
	for i in range(l1, r1):
		for j in range(l2, r2):
#			print(i, j)
			matrix[j][i] = elem

print_matrix(matrix)

#............%%%%%%%%%%
#............%%%%%%%%%%
#............%%%%%%%%%%
#.....#######%%%%%%%%%%
#.....##0####%%%%%%%%%%
#.....#######%%%%%%%%%%
#.....###1111111111%%%%
#.....###1111111111%%%%
#@@@@@@@@1111111111%%%%
#@@@@@@@@1111111111%%%%
#@@@@@@@@1111111111....
#@@@@@@@@1111111111....
#@@@@@@@@1111111111....
#@@@@@@@@1111111111....
#@@@@@@@@1111111111....
#@@@@@@@@1111111111....
#@@@@@@@@@@............
#@@@@@@@@@@............


#1 2 10 10 *
#-2 -1 10 10 #
#3 4 -10 10 @
#5 6 10 -10 %