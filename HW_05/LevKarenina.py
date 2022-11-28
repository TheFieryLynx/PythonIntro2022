#!/usr/bin/env python3

from collections import defaultdict
from collections import OrderedDict

pattern = input()
p = pattern[0]
b = pattern[1]
g = pattern[2]
e = pattern[3]

firstWord = defaultdict(int)
lastWord = defaultdict(int)
entries = OrderedDict()

firstMaxWordCnt = 0

lastMaxWordCnt = 0

end_of_string = ''

cnt = 1
while inp := input():
	s = inp.split()
	for i in range(len(s)):
		if i == 0:
			if end_of_string != '' and end_of_string[-1] == p:
				if s[i][0] == b:
					firstWord[s[i]] += 1
					if s[i] not in entries:
						entries[s[i]] = cnt
						cnt += 1
					if firstWord[s[i]] > firstMaxWordCnt:
						firstMaxWordCnt = firstWord[s[i]]
			end_of_string = s[-1]
		else:
			if s[i - 1][-1] == p:
				if s[i][0] == b:
					firstWord[s[i]] += 1
					if s[i] not in entries:
						entries[s[i]] = cnt
						cnt += 1
					if firstWord[s[i]] > firstMaxWordCnt:
						firstMaxWordCnt = firstWord[s[i]]
		if s[i][0] == g and s[i][-1] == e:
			lastWord[s[i]] += 1
			if lastWord[s[i]] > lastMaxWordCnt:
				lastMaxWordCnt = lastWord[s[i]]
			if s[i] not in entries:
				entries[s[i]] = cnt
				cnt += 1


fw = '...'
lw = '...'

flag1 = True

flag2 = True
for k, v in entries.items():
	if k in firstWord:
		if firstWord[k] == firstMaxWordCnt and flag1:
			fw = k
			flag1 = False
	if k in lastWord:
		if lastWord[k] == lastMaxWordCnt and flag2:
			lw = k
			flag2 = False
			
print(fw, firstMaxWordCnt, '-', lw, lastMaxWordCnt)
		