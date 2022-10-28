#!/usr/bin/env python3

def ADD(f, g):
	if callable(f):
		if callable(g):
			return lambda x: f(x) + g(x)
		else:
			return lambda x: f(x) + g
	else: 
		if callable(g):
			return lambda x: f + g(x)
		else:
			return lambda x: f + g

def SUB(f, g):
	if callable(f):
		if callable(g):
			return lambda x: f(x) - g(x)
		else:
			return lambda x: f(x) - g
	else: 
		if callable(g):
			return lambda x: f - g(x)
		else:
			return lambda x: f - g

def MUL(f, g):
	if callable(f):
		if callable(g):
			return lambda x: f(x) * g(x)
		else:
			return lambda x: f(x) * g
	else: 
		if callable(g):
			return lambda x: f * g(x)
		else:
			return lambda x: f * g

def DIV(f, g):
	if callable(f):
		if callable(g):
			return lambda x: f(x) / g(x)
		else:
			return lambda x: f(x) / g
	else: 
		if callable(g):
			return lambda x: f / g(x)
		else:
			return lambda x: f / g