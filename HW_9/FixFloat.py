#!/usr/bin/env python3

def fix(rounding):
	def decorator(function):
		def wrapper(*args, **kwargs):
			formattedArgs = [round(i, rounding) if isinstance(i, float) else i for i in args]
			for k, v in kwargs.items():
				kwargs[k] = round(v, rounding) if isinstance(v, float) else v
			ret = function(*formattedArgs, **kwargs)
			return round(ret, rounding) if isinstance(ret, float) else ret
		return wrapper
	return decorator
