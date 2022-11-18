#!/usr/bin/env python3

class morse:
	start_flag = [True]
	my_params = ["di", "dit", "dah"]
	last = ["."]
	signal_separator = [" "]
	alpha_separator = [", "]
	
	def __init__(self, buffer=""):
		if buffer == "":
#			print("kek: ", buffer)
			self.buffer = ""
			self.start_flag[0] = False
		elif buffer != "" and self.start_flag[0]:
#			print("MY PATTERN:", buffer)
			self.start_flag[0] = False
			self.buffer = ""
			inp = buffer.split()
			if len(inp) == 1:
				if len(buffer) == 2:
					self.my_params[0] = buffer[0]
					self.my_params[1] = buffer[0]
					self.my_params[2] = buffer[1]
				if len(buffer) == 3:
					self.my_params[0] = buffer[0]
					self.my_params[1] = buffer[1]
					self.my_params[2] = buffer[2]
				self.last[0] = ""
				if len(buffer) == 4:
					self.my_params[0] = buffer[0]
					self.my_params[1] = buffer[1]
					self.my_params[2] = buffer[2]
					self.last[0] = buffer[3]
				self.signal_separator[0] = ""
				self.alpha_separator[0] = " "
				
			if len(inp) == 2:
				self.my_params[0] = inp[0]
				self.my_params[1] = inp[0]
				self.my_params[2] = inp[1]
			if len(inp) == 3:
				self.my_params[0] = inp[0]
				self.my_params[1] = inp[1]
				self.my_params[2] = inp[2]
			if len(inp) == 4:
				self.my_params[0] = inp[0]
				self.my_params[1] = inp[1]
				self.my_params[2] = inp[2]
				self.last[0] = inp[3]
			
			if buffer[-1] == ' ':
				self.last[0] = ''
		
		elif buffer != "" and not self.start_flag[0]:
			self.buffer = buffer
		 
	def __neg__(self):
		return morse("-" + self.buffer)
	
	def __pos__(self):
		return morse("+" + self.buffer)
	
	def __invert__(self):
		return morse("~" + self.buffer)
	
	def __str__(self):
#		print(self.my_params)
#		print(self.buffer)
#		print(self.signal_separator)
#		print(self.alpha_separator)
#		print(self.last)
		res = ""
		
		for i in range(0, len(self.buffer) - 1):
#			print("'" + res + "'")
			if self.buffer[i] == '~':
				continue
			if self.buffer[i + 1] == '~' or i + 1 == len(self.buffer):
#				print(";" + res +";")
				if self.buffer[i] == '-':
					res += self.my_params[2]
				if self.buffer[i] == '+':
#					print("here")
					res += self.my_params[1]
				
				if self.buffer[i + 1] == '~':
					res += self.alpha_separator[0]
				
					
			elif self.buffer[i + 1] != '~':
				if self.buffer[i] == '-':
					res += self.my_params[2]
				if self.buffer[i] == '+':
					res += self.my_params[0]
				res += self.signal_separator[0]
		
		if len(self.buffer) != 0:
			if self.buffer[-1] == '-':
				res += self.my_params[2]
			if self.buffer[-1] == '+':
				res += self.my_params[1]
		res += self.last[0]
		
		
		self.start_flag[0] = True
		self.my_params[0] = "di"
		self.my_params[1] = "dit"
		self.my_params[2] = "dah"
		self.last[0] = "."
		self.signal_separator[0] = " "
		self.alpha_separator[0] = ", "
		return res
