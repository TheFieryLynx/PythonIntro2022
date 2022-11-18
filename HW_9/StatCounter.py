#!/usr/bin/env python3

from collections import OrderedDict

def statcounter():
	d = OrderedDict()
	
	in_proc = yield d
	
	def decorator(func):
		if func not in d:
			d[func] = 0
		def wrapper(*args, **kwargs):
			d[func] += 1
			return func(*args, **kwargs)
		return wrapper
	while in_proc:
		in_proc = yield decorator(in_proc)

#stat = statcounter()
#stats = next(stat)
#
#@stat.send
#def f1(a): return a+1
#	
#@stat.send
#def f2(a, b): return f1(a)+f1(b)
#	
#print(f1(f2(2,3)+f2(5,6)))
#print(*((f.__name__, c) for f, c in stats.items()))