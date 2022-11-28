#!/usr/bin/env python3

inp = int(input())
cnt = 0
cnt_tmp = 1
tmp = inp
while inp != 0:
	inp = int(input())
	if inp >= tmp:
		cnt_tmp += 1
	else:
		if cnt_tmp > cnt:
			cnt = cnt_tmp
		cnt_tmp = 1
	tmp = inp 
print(cnt)