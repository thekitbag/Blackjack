"""Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. 
For every digit that the user guessed correctly in the correct place, they have a cow. 
For every digit the user guessed correctly in the wrong place is a bull. 
Every time the user makes a guess, tell them how many cows and bulls they have. 
Once the user guesses the correct number, the game is over. 
Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.
"""

from random import randint
from time import sleep

guesses = 0
cows = 0
bulls = 0

print "Welcome to Cows and Bulls"
sleep(1)
print "I will think of a random 4 digit number and you must guess it." 
print "For each correct digit you guess in the right place you have a cow."
print "For each correct digit you guess in the wrong place you have a bull"
sleep(2)
print "Generating number..."
sleep(1)
solution = 5240
#randint(999,9999)

def checker(number):
	global cows
	global bulls
	global guesses		
	number = str(number)
	sol = str(solution)
	for digit in number:
		if digit in sol:
			bulls += 1		
	if digit[0] == sol[0]:
		cows += 1
		bulls -= 1
	if digit[1] == sol[1]:
		cows += 1
		bulls -= 1
	if digit[2] == sol[2]:
		cows += 1
		bulls -= 1	
	if digit[3] == sol[3]:
		cows += 1
		bulls -= 1		
		

	print "bulls = %s" %bulls	
	print "cows = %s" %cows
checker(4444)				

"""


	if number[0] == sol[0]:
		cows += 1
	elif number[0] in sol:
		bulls += 1		
	else: pass
	if number[1] == sol[1]:
		cows += 1
	elif number[1] in sol[2,4] or number[1] == sol[0]:
		bulls += 1		
	else: pass
	if number[2] == sol[2]:
		cows += 1
	elif number[2] in sol[0,2] or number[2] == sol[3]:
		bulls += 1		
	else: pass
	if number[3] == sol[3]:
		cows += 1
	elif number[3] in sol[0,3]:
		bulls += 1		
	else: pass
	guesses += 1
	print ""
	print "Cows: %s" %cows 
	print "Bulls: %s" %bulls 
	print "guesses: %s" %guesses
	print ""
	print "solution =", solution
	
while cows < 4:
	guess = raw_input("Guess a number:")
	cows = 0
	bulls = 0
	checker(guess)

print "You nailed it in %s guesses"	%guesses

		






"""


