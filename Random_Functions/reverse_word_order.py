"""Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

  My name is Michele
Then I would see the string:

  Michele is name My
shown back to me.
"""
def reverse_word_order():	
	phrase = raw_input("Give me a phrase and I'll return it to you with the words reversed!")
	words = phrase.split()
	new_words = []
	for i in reversed(words):
			new_words.append(i)
	new_words = " ".join(new_words)		
	return new_words		
			
print reverse_word_order()