#Blackjack game
import random 

shoe = []
player_hand = []
dealer_hand = []
player_score = 0
dealer_score = 0
player_bust = False
player_sticks = False
blackjack = False

def create_shoe(decks):
#creates a shoe of X standard 52 card decks
	ranks = ["A","2","3","4","5","6","7","8","9","T","J","Q","K",]
	suits = ["c","d","h","s"]
	for i in range(decks):
		for i in ranks:		
				shoe.append(i + suits[0])
				shoe.append(i + suits[1])
				shoe.append(i + suits[2])
				shoe.append(i + suits[3])			
	
def shuffle():
	random.shuffle(shoe)

def deal():
	for i in range(2):
		player_hand.append(shoe.pop())
		dealer_hand.append(shoe.pop())
	
def evaluate_score(hand):
	global blackjack
	score = 0
	values = []
	pictures = ["T","J","Q","K"]
	for i in range(len(hand)):
		values.append(hand[i][0])
	for k in values:
		if k == "A":
			score += 11
		elif k in pictures:
			score += 10
		else:
			score += int(k)
	if "A" not in values:
		return score
	else:
		if len(hand) == 2 and score == 21:
			blackjack = True
		elif score < 22:
			return score
		else:
			for x in values:
				if x == "A":
					if score > 21:
						score -= 10
			return score

def update_scores():
	global player_score
	global dealer_score
	global player_bust
	player_score = evaluate_score(player_hand)
	dealer_score = evaluate_score(dealer_hand)
	if player_score > 21:
		player_bust = True

def declare():
	update_scores()
	if blackjack == True:
		print ""
	if player_bust == True:
		print ""
		print "Player hand:", player_hand
		print ""
		print "Dealer's up-card:", dealer_hand[0]
		print ""
		print "You have", player_score				
	else:		
		print "Player hand:", player_hand
		print ""
		print "Dealer's up-card:", dealer_hand[0]
		print ""
		print "You have", player_score	
		print ""
		print "your options are", possible_actions(player_hand,player_score)
		print ""

def possible_actions(hand,score):
	options = ["Hit", "Stick"]
	blackjack = False
	if hand[0][0] == hand[1][0]:
		options.append("Split")
	if 12 > score > 8:
		options.append("Double")
	if score == 21:
		blackjack = True	
	if blackjack == False:
		return options
	else:
		return "Blackjack! Congratulations, you win."

def ask_action():
	player_action = raw_input("Choose an option:")
	if player_action.lower() == "hit":
		hit()
	elif player_action.lower() == "stick":
		stick()
	elif player_action.lower() == "double":
		double()
	elif player_action.lower() == "split":
		split()

def hit():
	player_hand.append(shoe.pop())

def stick():
	global player_sticks
	player_sticks = True

print ""
print "Welcome to Blackjack"
print ""
print ""

create_shoe(6)
shuffle()
deal()
declare()
if blackjack == False:
	while player_bust == False and player_sticks == False:
		ask_action()
		declare()	
	if player_bust == True:
		print ""
		print "Player bust, Dealer wins"
	else:
		print "Player Sticks"
else:
	print "Blackjack! Player wins"






#tests
#print "There are", len(shoe), "remaining cards in the shoe"

"""
bugs
tells you your options and says you have None when you hit blackjack

to-do
create two card special situations - blackjack, split, double, perfect pair, 21 + 3
DRY in declare function
deal with invalid inputs
dealer play
Make Start game a function
Be able to split two pictures but not A9
betting
test

"""