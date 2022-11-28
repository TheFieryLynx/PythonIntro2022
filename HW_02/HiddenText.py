#!/usr/bin/env python3

str1 = input()
str2 = input()

len1 = len(str1)
len2 = len(str2)

delta = 1

str2_ind = 0
flag = False

if len2 > len1:
	print('NO')
	exit(0)
	
if len1 == 0 or len2 == 0:
	print('YES')
	exit(0)

for i, v in enumerate(str1):
	if v == str2[str2_ind]:
		if len2 == 1:
			print('YES')
			exit(0)
		str2_ind = str2_ind + 1
		for j in range(i + 1, len(str1)):
			if str1[j] == str2[str2_ind]:
				if len2 == 2:
					print('YES')
					exit(0)
				delta = j - i
				break
		str2_ind = str2_ind + 1
		for k in range(i + 2 * delta, len(str1), delta):
			if str1[k] == str2[str2_ind]:
				str2_ind = str2_ind + 1
			else:
				flag = True
			
			if str2_ind == len2:
				print('YES')
				exit(0)
	else:
		if len2 == 1 and len1 == 1:
			print('NO')
			exit(0)
		str2_ind = 0
else:
	print('NO')
	exit(0)
	
if flag:
	print('NO')