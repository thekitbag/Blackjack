#recipemate
import random
import sqlite3


db = 'recipe_db.sqlite' 

def add_column(table, column, datatype):
	#adds a column to an exisiting table
	conn = sqlite3.connect(db)
	c = conn.cursor()

	c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
	        .format(tn=table, cn=column, ct=datatype))

	conn.commit()
	conn.close()

def query(table, column, field):
	#returns the whole row from the given table where field is in the given column
	conn = sqlite3.connect(db)
	c = conn.cursor()
	c.execute('SELECT * FROM {tn} WHERE {cn} = "{cv}"'.\
        format(tn=table, cn=column, cv=field))
	all_rows = c.fetchall()
	print('1):', all_rows)

def insert_row():
		#adds a new row to an existing table
		conn = sqlite3.connect(db)
		c = conn.cursor()


def set_mode():
	choice = raw_input("What do you want to do. Type 1 to add a column to an existing table or 2 to run a query:  ")
	if choice == "1":
		table = raw_input("Which table?  ")
		column = raw_input("What's the column name?  ")
		datatype = raw_input("What data type will be in the column? INTEGER, TEXT, NULL, REAL, BLOB  ")
		add_column(table, column, datatype)
	elif choice == "2":
		table = raw_input("Which table do you want to query?  ")
		column = raw_input("Which column do you want to look at?  ")
		field = raw_input("what value are you looking for?  ")
		query(table, column, field)
	else:
		print "Was that an option? NO!" 			


set_mode()









"""
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
	



def gffinder(meal):
		if meal.gluten == True:
			return False
		else:
			return True	

def randomise():
	return random.choice(recipe_list)			












"""
