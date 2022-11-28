#!/usr/bin/env python3

from collections import OrderedDict

class Spiral:
	
	def __init__(self, buffer=""):
		self.buffer = buffer
		self.order = OrderedDict()
		for i in buffer:
			if i not in self.order:
				self.order[i] = 1
			else:
				self.order[i] += 1
		
	def __iter__(self):
		for i in self.buffer:
			yield i
			
	def __add__(self, other):
		d = self.order.copy()
		for k, v in other.order.items():
			if k in d:
				d[k] += v
			else:
				d[k] = v
		buffer = ''
		for k in d:
			buffer += k * d[k]
		return Spiral(buffer)
	
	def __sub__(self, other):
		d = self.order.copy()
		for k, v in d.items():
			if k in other.order:
				d[k] -= other.order[k]
				if d[k] < 0:
					d[k] = 0
		buffer = ''
		for k in d:
			buffer += k * d[k]
		return Spiral(buffer)

	
	def __mul__(self, other):
		d = self.order.copy()
		for k, v in d.items():
			d[k] = v * other
		buffer = ''
		for k in d:
			buffer += k * d[k]
		return Spiral(buffer)
	
	def __str__(self):
		l = len(self.buffer)
		
#		print(l)
		left = -1
		right = 0
		i = 1
#		print(i, ": [", left, right, ']')
		while True:
			tmp = right + i
			left = right
			right = tmp
			
#			print(i, ": [", left, right, ']')
			if right > l - 1:
				break
			i += 1
			
#		print(left, right, i)
		width = 0
		height = 0
		
		if i % 2 == 1:
			width = i + 1
			height = i
			if l == right:
				width -= 1
			if l <= right - 1:
				width -= 2
		else:
			width = i
			height = i + 1
			if l == right:
				height -= 1
			if l <= right - 1:
				height -= 2
		if l == 1:
			width = 1
			height = 1
#		print(width, height)
		
		matrix = [ [' '] * width for i in range(height) ]
		
		direction = 0
		# 0 - left
		# 1 = bottom
		# 2 - right
		# 3 - top
		
		x = 0
		y = 0
		if i % 4 == 1:
			x = l - left - 1
			y = height - 1
			direction = 0
		if i % 4 == 2:
			x = width - 1
			y = height - (l - left)
			direction = 1
		if i % 4 == 3:
			x = width - (l - left)
			y = 0
			direction = 2
		if i % 4 == 0:
			x = 0
			y = width - (right - l) - 1
			direction = 3
		save_i = i
		if width == 1 and height == 1:
			x = 0
			y = 0
#		print(x, y)
#		print("========")
#		matrix[y][x] = str(l)
		index = len(self.buffer) - 1
		first = True
		cnt = l - left
		exit = False
		while True:
#			print(direction)
			for i in range(cnt):
#				print(cnt, i, direction)
#				print(matrix)
				if direction == 0:
					matrix[y][x] = self.buffer[index]
					index -= 1
					if index == -1:
						exit = True
						break
					x -= 1
				if direction == 1:
					matrix[y][x] = self.buffer[index]
					index -= 1
					if index == -1:
						break
					y += 1
				if direction == 2:
					matrix[y][x] = self.buffer[index]
					index -= 1
					if index == -1:
						break
					x += 1
				if direction == 3:
					matrix[y][x] = self.buffer[index]
					index -= 1
					if index == -1:
						break
					y -= 1
#				print(x, y)
#			print(direction)
			if direction == 0:
				x += 1
				y -= 1
				direction = 3
			elif direction == 3:
				y += 1
				x += 1
				direction = 2
			elif direction == 2:
				x -= 1
				y += 1
				direction = 1
			elif direction == 1:
				y -= 1
				x -= 1
				direction = 0
			if first:
				first = False
				cnt = save_i - 1
			else:
				cnt -= 1
				
			if exit:
				break
#			print(cnt, save_i, direction)
		
#		print(matrix)
#		print('\n')
		
		res = ''
		for row in range(len(matrix)):
			for i in matrix[row]:
				res += i
			if row != len(matrix) - 1:
				res += '\n'
		
		matrix.clear()
		return res		
#S = Spiral("abbcccddddeeeee")
#I = Spiral("abcdefghi")

#print(f"{S}\n")
#print(S+I, "\n")
#print(S-I, "\n")
#print(I*2, "\n")
#print(I*2-S, "\n")
#print(*list(S+I))

#import random, string
#random.seed(42)
#A, B =(Spiral("".join(sorted(random.choices(string.ascii_letters, k=1000)))) for i in range(2))
#print(A+Spiral(""))
#print(B+Spiral("1"))
#print(Spiral("2")+A+B)
#print(Spiral("3")+A-B*2)
#print(B*2-A*3+Spiral("0"))
#print("".join(A)+"".join(B))