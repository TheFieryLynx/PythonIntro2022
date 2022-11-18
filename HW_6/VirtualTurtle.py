#!/usr/bin/env python3

def turtle(coord, direction):
	c = list(coord)
	inp = yield tuple(c)
	while inp:
		if inp == 'f':
			if direction == 0:
				c[0] += 1
			elif direction == 1:
				c[1] += 1
			elif direction == 2:
				c[0] -= 1
			elif direction == 3:
				c[1] -= 1
		elif inp == 'l':
			if direction == 0:
				direction = 1
			elif direction == 1:
				direction = 2
			elif direction == 2:
				direction = 3
			elif direction == 3:
				direction = 0
				
		elif inp == 'r':
			if direction == 0:
				direction = 3
			elif direction == 3:
				direction = 2
			elif direction == 2:
				direction = 1
			elif direction == 1:
				direction = 0
		inp = yield tuple(c)
	
#robo = turtle((0, 0), 0)
#start = next(robo)
#for c in "flfrffrffr":
#	print(*robo.send(c))
#		
#robo = turtle((0,0),0)
#start = next(robo)
#for c in "flfrffrffr":
#	print(*robo.send(c))