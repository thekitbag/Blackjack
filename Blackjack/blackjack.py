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
player_wins = False
push = False

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
		if score < 22:
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
	global blackjack
	player_score = evaluate_score(player_hand)
	dealer_score = evaluate_score(dealer_hand)
	if player_score > 21:
		player_bust = True
	if player_score == 21 and len(player_hand) == 2:
		blackjack = True
def spaces(number):
	print ""*number


def initial_declare():
	global blackjack
	update_scores()	
	spaces(3)
	print "                             Welcome to Blackjack"
	spaces(2)		
	print "Player hand:", player_hand
	spaces(1)
	print "Dealer's up-card:", dealer_hand[0]
	spaces(1)
	if blackjack == True:
		print "Blackjack! Player wins!"
	else:
		print "You have", player_score
		spaces(1)
		print "your options are", possible_actions(player_hand,player_score)	
	spaces(1)	

def declare():
	update_scores()
	if player_bust == True:
		spaces(1)
		print "Player hand:", player_hand
		spaces(1)
		print "Dealer's up-card:", dealer_hand[0]
		spaces(1)
		print "You have", player_score, 
		print "Player bust. Dealer wins"
	elif player_sticks == True:
		spaces(1)
		print "Player sticks on", player_score					
	else:
		spaces(1)		
		print "Player hand:", player_hand
		spaces(1)
		print "Dealer's up-card:", dealer_hand[0]
		spaces(1)
		print "You have", player_score	
		spaces(1)
		print "your options are", possible_actions(player_hand,player_score)
		spaces(1)

def phase_two_declare():
	update_scores()
	spaces(1)		
	print "Player hand:", player_hand
	spaces(1)
	print "Dealer's up-card:", dealer_hand
	spaces(1)
	print "Player_score:", player_score
	print "Dealer has", dealer_score	
	spaces(1)

def final_declare():
	if player_wins == True:
		print spaces(2)
		print "Player wins!"
	elif push == True:
		print spaces(2)
		print "Push"
	else:
		print spaces(2)
		print "Dealer wins"
			



def possible_actions(hand,score):
	options = ["Hit", "Stick"]
	if hand[0][0] == hand[1][0]:
		options.append("Split")
	if 12 > score > 8:
		options.append("Double")
	return options	
	

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

def dealer_play():
	dealer_hand.append(shoe.pop())

def evaluate_winner():
	global player_wins
	global push
	if dealer_score > 21:
		player_wins == True
	elif dealer_score > player_score:
		player_wins = False
	elif player_score > dealer_score:
		player_wins = True	
	else:
		push = True	


create_shoe(6)
shuffle()
deal()
initial_declare()
while player_bust == False and player_sticks == False and player_score < 21:
		ask_action()
		declare()
if player_bust == False:		
	phase_two_declare()
	while dealer_score < 17:
		dealer_play()
		phase_two_declare()
evaluate_winner()
final_declare()		


"""
print spaces(5)
print "player_hand=",player_hand
print "dealer_hand=", dealer_hand 
print "player_score=", player_score
print "dealer_score=", dealer_score
print "player_bust=", player_bust 
print "player_sticks=", player_sticks
print "blackjack=", blackjack 
print "player_wins=", player_wins 
print "push=", push 	
"""

	






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