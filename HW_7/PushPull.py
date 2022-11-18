#!/usr/bin/env python3

class Pushpull:
	steps = [0]
	
	def __init__(self, n = 0):
		self.steps[0] = n
		
	def push(self, r = 1):
		self.steps[0] += r
	
	def pull(self, l = 1):
		self.steps[0] -= l
		
	def __iter__(self):
		sign = 1
		if self.steps[0] < 0:
			sign = -1
			
		for i in range(0, self.steps[0], sign):
			yield i
		pass
	
	def __str__(self):
		if self.steps[0] < 0:
			return '<' + str(abs(self.steps[0])) + '<'
		elif self.steps[0] == 0:
			return '<' + str(self.steps[0]) + '>'
		elif self.steps[0] > 0:
			return '>' + str(self.steps[0]) + '>'
			
			
	
#a = Pushpull(-10)
#print(a)
#b, c = Pushpull(7), Pushpull(5)
#print(b)
#for i in b:
#	c.pull()
#print(a)
#b.push(3)
#t = tuple(c)
#a.pull(7)
#t += tuple(b)
#print(*t)
	