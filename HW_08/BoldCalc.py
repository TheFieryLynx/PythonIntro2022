#!/usr/bin/env python3

nums = '0123456789'
alph = 'abcdefghijklmnopqrstuvwxyz'
alph_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
operations = '(+-*/%)'
extra = '_'
symbols = nums + alph + alph_upper + operations + extra
custom_globals = dict()
	
def change_vars(str):
	res = ''
	for i in str:
		res += '_' + i if i.isalpha() else i
	res = res.replace('/', '//')
	return res

	
def check_expression(str):
	if '**' in str:
		raise SyntaxError
	for i in range(len(str)):
		if str[i] not in symbols:
			raise SyntaxError
		if str[i] == '(':
			if i != 0:
				if str[i - 1] not in operations:
					raise SyntaxError
		if str[i] == ')':
			if i != len(str) - 1:
				if str[i + 1] not in operations:
					raise SyntaxError
	
while inp := input():
	inp = "".join(inp.split())
	try:
		if inp[0] != '#':
			expression = inp.split('=')
			l = len(expression)
			if l == 1:
				check_expression(expression[0])
				expression[0] = change_vars(expression[0])
				print(eval(expression[0], custom_globals))
			elif l == 2:
				if not expression[0].isidentifier():
					raise AssertionError
				for i in expression[0]:
					if i not in symbols:
						raise SyntaxError
				check_expression(expression[1])
				expression[0] = change_vars(expression[0])
				expression[1] = change_vars(expression[1])
				custom_globals[expression[0]] = eval(expression[1], custom_globals)
			else:
				raise SyntaxError
	except SyntaxError:
		print("Syntax error")
	except AssertionError:
		print("Assignment error")
	except NameError:
		print("Name error")
	except Exception:
		print("Runtime error")
			