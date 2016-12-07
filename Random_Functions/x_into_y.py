"""Ask the user for a number. Depending on whether the number is 
even or odd, print out an appropriate message to the user. 


Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) 
and one number to divide by (check). If check divides evenly into num, 
tell that to the user. If not, print a different appropriate message.
"""
print "Enter two numbers and I'll tell you if the first is divisible by the second"
my_dividend = float(raw_input("First number please:"))
my_divisor = float(raw_input("Great. and the second number please:"))
div = my_dividend / my_divisor

print "You want to know if", my_dividend, "goes into", my_divisor

if my_dividend % my_divisor == 0:
	print "it sure does", my_dividend, "divided by", my_divisor, "is equal to", div
else:
	print "No it doesn't", my_dividend, "divided by", my_divisor, "is equal to", div