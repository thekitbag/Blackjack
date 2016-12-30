from lunchbuddy import *
program_running = True
a = Admin()
b = Actions()

def options_menu():
	global program_running	
	print 	""	
	print	"How can I help you?"
	print	""
	print	"1: Get help finding a lunch destination"
	print   "2: Log a lunch experience"
	print	"0: exit program"
	print   ""
	choice = raw_input(">")
	if choice == "1":
		print 	""
		print	"Great. Choose an option below"
		print	""
		print	"1: list all restaurants"
		print   "2: pick a random restaurant"
		print   "3: look for a restaurant that matches a certain criteria"
		print   "0: go to previous menu"
		print   ""
		second_choice = raw_input(">")
		if second_choice == "1":
			b.list_all("restaurants")
		elif second_choice == "2":
			print "WIP"
		elif second_choice == "3":
			b.lookup()
		else:
			print "dude, was that an option?"			
	elif choice == "2":
		b.log()
	elif choice == "0":
		program_running = False	
		print ""
		print "Laters"
	else:
		print ""
		print "Was that an option? NO!"	




def run_program():
	print ""
	print "Welcome to lunch buddy. too lazy to think up where to go for lunch? I'll try to help"
	while program_running == True:
		options_menu()

run_program()


