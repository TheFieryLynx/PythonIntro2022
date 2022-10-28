#!/usr/bin/env python3

def No_2Zero(N, K):
	def f(N):
		if N == 1:
			return K - 1
		if N == 2:
			return K ** 2 - K
		return (K - 1) * (f(N - 1) + f(N - 2))
	return f(N)
	