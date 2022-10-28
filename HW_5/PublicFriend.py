#!/usr/bin/env python3

friends = dict()
friends_set = set()

M, N = map(int, input().split(sep = ', '))
while True:
	if M == 0 and N == 0:
		break
	friends_set.add(M)
	friends_set.add(N)
	if M in friends:
		friends[M].add(N)
	else:
		friends[M] = { N }
	
	if N in friends:
		friends[N].add(M)
	else:
		friends[N] = { M }
		
	M, N = map(int, input().split(sep = ', '))

friends_list = list()
cnt = len(friends)


for k, v in friends.items():
	if len(v) == cnt - 1:
		friends_list.append(k)

print(*sorted(friends_list))
