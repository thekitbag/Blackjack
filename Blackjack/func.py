def create_shoe(decks):
#creates a shoe of X standard 52 card decks
	shoe  = []
	ranks = ["A","2","3","4","5","6","7","8","9","T","J","Q","K",]
	suits = ["c","d","h","s"]
	for i in range(decks):
		for i in ranks:		
				shoe.append(i + suits[int(i)])
	return shoe

print create_shoe(1)					
