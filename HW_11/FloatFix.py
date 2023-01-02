#!/usr/bin/env python3

import types, numbers

class fixed(type):
	@staticmethod
	def __new__(metacls, name, parents, ns, ndigits=3):
		def decorator(function):
			def wrapper(*args, **kwargs):
#				formattedArgs = [round(i, ndigits) if isinstance(i, numbers.Real) else i for i in args]
#				for k, v in kwargs.items():
#					kwargs[k] = round(v, ndigits) if isinstance(v, numbers.Real) else v
				ret = function(*args, **kwargs)
				return round(ret, ndigits) if isinstance(ret, numbers.Real) else ret
			return wrapper
		for i in ns:
			if isinstance(ns[i], types.FunctionType):
				ns[i] = decorator(ns[i])
		return super().__new__(metacls, name, parents, ns)
	
#from fractions import Fraction
#from decimal import Decimal
#
#class C(metaclass=fixed, ndigits=4):
#	def div(self, a, b):
#		return a / b
#	
#print(C().div(6, 7))
#print(C().div(Fraction(6), Fraction(7)))
#print(C().div(Decimal(6), Decimal(7)))
#	
#import numbers
#class ffix(numbers.Real.__class__, fixed): pass
#class numnum(complex, numbers.Real, metaclass=ffix):
#	def __round__(self, ndigits=12):
#		return 42
#	def __neg__(self):
#		return self
#	def __str__(self):
#		return "987.645321234"
#	
#print(numnum())
#print(-numnum())