#!/usr/bin/env python3
from functools import cmp_to_key

def compare(person1, person2):
	if person1[-1] != person2[-1]:
		tm1 = list(map(int, person1[-1].split(':')))
		tm2 = list(map(int, person2[-1].split(':')))
		if tm1[0] == tm2[0]:
			if tm1[1] == tm2[1]:
				return tm1[2] - tm2[2]
			else:
				return tm1[1] - tm2[1]
		else:
			return tm1[0] - tm2[0]
	else:
		if person1[1] < person2[1]:
			return -1
		elif person1[1] > person2[1]:
			return 1
		else:
			if person1[0] < person2[0]:
				return -1
			elif person1[0] > person2[0]:
				return 1
			else:
				if person1[2] < person2[2]:
					return -1
				elif person1[2] > person2[2]:
					return 1
				return 0
		return 0
	return 0

zen_leaders = list()
inp = input()
while inp != '':
	tmp = inp.split(sep=' ')
	if len(tmp) == 4:
		zen_leaders.append(tmp)
	else:
		tmp_list = list()
		tmp_list.append(tmp[0])
		tmp_list.append(tmp[1])
		tmp_list.append(' '.join(tmp[2: -1]))
		tmp_list.append(tmp[-1])
		zen_leaders.append(tmp_list)
	inp = input()
	
	
zen_leaders.sort(key=cmp_to_key(compare))
place = 0
cnt = -1
cmp_time = ''

l = [-1] * 4 

for i, elem in enumerate(zen_leaders):
	for j in range(len(elem)):
		if len(elem[j]) > l[j]:
			l[j] = len(elem[j])
	if i == 0:
		place += 1
		cmp_time = elem[-1]
	else:
		if elem[-1] != cmp_time:
			cmp_time = elem[-1]
			place += 1
			if place == 4:
				cnt = i
				break
if cnt == -1:
	cnt = len(zen_leaders)

for i in range(cnt):
	for j in range(4):
		print('{:<{prec}}'.format(zen_leaders[i][j], prec=l[j]), end=' ')
	print()