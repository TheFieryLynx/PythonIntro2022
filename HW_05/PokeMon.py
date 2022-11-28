#!/usr/bin/env python3

playersToDecks = dict()
decksToCards = dict()

playersCardsCnt = dict()

while inp := input():
	a, b = inp.split(sep=' / ')
	if a.isdigit():
		if a in decksToCards:
			decksToCards[a].add(b)
		else:
			decksToCards[a] = { b }
	else:
		if a in playersToDecks:
			playersToDecks[a].add(b)
		else:
			playersToDecks[a] = { b }

max_cards = 0

for player, decks in playersToDecks.items():
	playersCards = set()
	for deck in decks:
		playersCards = playersCards.union(decksToCards[deck])
			
	playersCardsCnt[player] = len(playersCards)
	if playersCardsCnt[player] > max_cards:
		max_cards = playersCardsCnt[player]
	
result = sorted(list(filter(lambda a: playersCardsCnt[a] == max_cards, playersCardsCnt)))
for i in sorted(result):
	print(i)
