#!/usr/bin/env python3

class Nuts():
	def __init__(self, *args):
		self.params = args
		
	def __str__(self):
		return "Nuts"
	
	def __getitem__(self, i):
		return i
	
	def __setitem__(self, key, value):
		pass
	
	def __iter__(self):
		for i in 'Nuts':
			yield i
		
	def __del__(self):
		pass
		
	def __delitem__(self, key):
		pass
		
	def __delattr__(self, key):
		pass

	
	def __getattribute__(self, item):
		return item
		
#M, N = Nuts(), Nuts(1,2,3,4)
#print(M, N)
#N.qwerty
#M[100] = N.qwerty = 42
#print(M[100], N.qwerty)
#print(*list(Nuts("QWERQWERQWER")))
#del M["QQ"], N[6:10], M[...], N._, N.qwerty
#print(M.asdfg, N[-2])