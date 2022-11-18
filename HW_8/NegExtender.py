#!/usr/bin/env python3

class NegExt:
#	def __init__(self):
		
	def __neg__(self):
		try:
			return self.__class__(self.__class__.mro()[2].__neg__(self))
		except:
			try:
				return self.__class__(self[1:-1])
			except:
				return self.__class__(self)

#class nstr(NegExt, str):
#	pass
#class nnum(NegExt, int):
#	pass
#class ndict(NegExt, dict):
#	pass
#print(-nstr("Python"), -nnum(123), -ndict({1: 2, 3: 4}), --nstr("NegExt"))
#			
#class C:
#	def __init__(self, val="A_b"):
#		self.val = str(val) * 2
#	def __str__(self):
#		return self.val
#	
#class D(NegExt, C):
#	pass
#	
#print(-D(), --D())

#class C:
#	def __init__(self, val=0):
#		self.val = val
#	def __neg__(self):
#		return self.val * 2
#	def __str__(self):
#		return str(self.val)
#	
#class E(C):
#	pass
#	
#class D(NegExt, E):
#	pass
#	
#for i in range(100500):
#	res = --D(1)
#print(i, res)