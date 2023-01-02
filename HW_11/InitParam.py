#!/usr/bin/env python3

import types
import inspect

class init(type):
	@staticmethod
	def __new__(metacls, name, parents, ns, **kwds):
		for i in ns:
			if isinstance(ns[i], types.FunctionType):
#				print(inspect.get_annotations(ns[i]))
#				print(inspect.getfullargspec(ns[i])[3])
#				print(inspect.signature(ns[i]).parameters)
#				print(ns[i].__annotations__.items())
#				
				defaults = []
				for k, v in inspect.get_annotations(ns[i]).items():
#					print(k)
#					print(ns)
#					print('kek', inspect.signature(ns[i]).parameters[str(k)].default)
					try:
						tmp = inspect.signature(ns[i]).parameters[str(k)].default
						if inspect.signature(ns[i]).parameters[str(k)].default is not inspect.Parameter.empty:
							defaults.append(tmp)
						else:	
							defaults.append(v())
					except:
						defaults.append(None)
				ns[i].__defaults__ = tuple(defaults)
					
			
		return super().__new__(metacls, name, parents, ns)
		
#class C(metaclass=init):
#	def __init__(self, var: int, rng: range, lst: list[int], defined: str = "defined"):
#		self.data = f"{var}/{rng}/{lst}/{defined}"
#		
#for c in (C(), C(1, range(3)), C(rng=range(4, 7)), C(lst=[1, 2, 3], defined=3)):
#	print(c.data)