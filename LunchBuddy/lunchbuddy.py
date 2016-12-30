#recipemate
from random import randint
import time
import sqlite3
db = 'H:\Coding\LunchBuddy\lunchbuddy.sqlite' 
conn = sqlite3.connect(db)
c = conn.cursor()


"""to do list

"""
class Admin(object):

	def create_table(self, tablename, column, datatype):
		#creates a new table in recipe_db.sqlite
		self.tablename = tablename
		self.column = column
		self.datatype = datatype
		conn = sqlite3.connect(db)
		c = conn.cursor()
		c.execute("CREATE table {tn} (ID 'INTEGER', {cn} {ct})"\
		        .format(tn=tablename, cn=column, ct=datatype))
		conn.commit()
		conn.close()

	def add_column(self, table, column, datatype):
		#adds a column to an exisiting table
		self.table = table
		self.column = column
		self.datatype = datatype
		conn = sqlite3.connect(db)
		c = conn.cursor()
		c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
		        .format(tn=table, cn=column, ct=datatype))
		conn.commit()
		conn.close()

	def insert_row(self, table, column, field):
		#adds a new row to an existing table
		self.table = table
		self.column = column
		self.field = field
		row_id = row_count + 1
		conn = sqlite3.connect(db)
		c = conn.cursor()
		c.execute('INSERT INTO {tn} (ID, {cn}) VALUES ({row}, "{ct}")'\
		        .format(tn=table, cn=column, row=row_id, ct=field))
		conn.commit()
		conn.close()

	def update_row(self, table, column, field, icol, ival):
		#adds a new row to an existing table
		self.table = table
		self.column = column
		self.field = field
		self.icol = icol
		self.ival = ival
		conn = sqlite3.connect(db)
		c = conn.cursor()
		c.execute('UPDATE {tn} SET {cn} = {field} WHERE {icol} = {ival}'\
		        .format(tn=table, cn=column, field=field, icol=icol, ival=ival))
		conn.commit()
		conn.close()

class Actions():		

	def lookup(self):
		#returns the names of all the resturants that martch a certain criteria				
		column = raw_input("What is your search criteria?")
		field = raw_input("Which value are you looking for?")
		conn = sqlite3.connect(db)
		c = conn.cursor()
		c.execute('SELECT * FROM restaurants WHERE {cn} = "{cv}"'.\
	        format(cn=column, cv=field))
		all_rows = c.fetchall()
		print ""
		for i in all_rows:
			print i[1]

	def log(self):
		#allows the user to log a restaurant and its rating out of ten along with today's date
		place = raw_input("Where did you eat?").lower()
		rating = raw_input("How was it on a scale of 1-10")
		date = time.strftime("%d/%m/%Y")
		conn = sqlite3.connect(db)
		conn.text_factory = str
		c = conn.cursor()
		c.execute('insert into visits values ("{p}", "{d}", {r})'.\
	        format(p=place, d=date, r=rating))
		conn.commit()
		conn.close()

	def list_all(self, table):
		self.table = table
		conn = sqlite3.connect(db)
		c = conn.cursor()
		c.execute('SELECT * FROM {t}'.\
	        format(t=table))
		all_rows = c.fetchall()		
		for i in all_rows:
			print i[1]


	










"""


def run_program():
	program_running = True
	a = Admin()
	b = Actions()
	print "Welcome to lunch buddy. too lazy to think up where to go for lunch? I'll try to help"
	def options_menu():		
		print	"1: View all options"
		print	"0: exit program"
		choice = raw_input("")
		if choice == "1":
			print "WIP"
		elif choice == "0":
			program_running = False	
			print "Laters"
		else:
			print "Was that an option? NO!"
	print "What do you want to do next?"	
	options_menu()


class Recipe(object):	
	#mealtypes="lunch", "lunch/dinner", "dinner"
	def __init__(self, ingredients, preptime, mealtype, gluten):
		self.ingredients = ingredients
		self.preptime = preptime
		self.mealtype = mealtype
		self.gluten = gluten

	def __repr__(self):
		print "ME"


risotto = Recipe(['onions', 'bacon', 'parmesan', 'peas', 'vegetable stock', 'risotto rice'], 30, 'dinner', False)
chicken_stirfry = Recipe(['chicken', 'onion', 'cornflour', 'chicken stock', 'sugar snap peas', 'peppers', 'brown sugar', 'soy sauce', 'rice noodles'], 30, 'dinner', False)
breaded_chicken = Recipe(['chicken', 'breadcrumbs', 'crushed chillies', 'salad', 'cheese'], 30, 'dinner', False)
pesto_pasta = Recipe(['pasta, pesto'], 15, 'lunch/dinner', True)		


recipe_list = [
risotto, 
chicken_stirfry, 
breaded_chicken, 
pesto_pasta
]

class Mode(object):
	pass
	














"""
