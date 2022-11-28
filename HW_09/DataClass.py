#!/usr/bin/env python3

def sloter(fields, default):
	class data:
		def __init__(self):
			for i in fields:
				self.__dict__[i] = default
				
		def __iter__(self):
			for i in fields:
				yield self.__dict__[i]
				
		def __delattr__(self, field):
			self.__dict__[field] = default
		
		def __setattr__(self, field, value):
			if field not in self.__dict__:
				raise AttributeError
			else:
				self.__dict__[field] = value
	return data
