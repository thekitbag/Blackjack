#recipemate
from random import randint
import sqlite3
db = 'recipe_db.sqlite' 
conn = sqlite3.connect(db)
c = conn.cursor()
c.execute("SELECT count(*) FROM 'recipes'")
row_count = c.fetchone()[0]


"""to do list
move pritn statements out of run_program() and into their respective functions
allow admin functions to accept a dictionary of data: datatype pairs
create second table which is a big db of recipes from the internet
allow the user to get the quickest, or the lowest calorie. and how many of them to fetch
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

	def query(self, table, column, field):
		#returns the whole row from the given table where field is in the given column
		self.table = table
		self.column = column
		self.field = field
		conn = sqlite3.connect(db)
		c = conn.cursor()
		c.execute('SELECT title, ingredients FROM {tn} WHERE {cn} = "{cv}"'.\
	        format(tn=table, cn=column, cv=field))
		all_rows = c.fetchall()
		print all_rows

	def ingredients_search(ingredient):
		#asks the user for ana ingredient and searches the db for recipes that contain
		ingredient = raw_input("name an ingredient that you already have, in lower case ")	
		conn = sqlite3.connect(db)
		conn.text_factory = str
		c = conn.cursor()
		c.execute('SELECT title FROM {tn} where {cn} like "%{cv}%"'.\
	        format(tn='recipes', cn='ingredients', cv= ingredient))
		all_titles = c.fetchall()
		d = conn.cursor()
		d.execute('SELECT ingredients FROM {tn} where {cn} like "%{cv}%"'.\
	        format(tn='recipes', cn='ingredients', cv= ingredient))
		all_ingredients = d.fetchall()
		print all_titles


	def randomise(self):
		#returns a random recipe to the user
		num = randint(1,row_count)
		conn = sqlite3.connect(db)
		conn.text_factory = str
		c = conn.cursor()
		c.execute('SELECT title FROM {tn} where {cn} = "{cv}"'.\
	        format(tn='recipes', cn='ID', cv= num))
		recipe = c.fetchall()
		print recipe


def run_program():
	program_running = True
	a = Admin()
	b = Actions()
	while program_running == True:
		print "What do you want to do next? type the number on the left for the thing on the right:"
		print	"1: add a column"
		print	"2: run a query"
		print	"3: get a random recipe"
		print	"4: look up recipes with a speific ingredient"
		print	"0: exit program"
		choice = raw_input("")
		if choice == "1":
			table = raw_input("Which table?  ")
			column = raw_input("What's the column name?  ")
			datatype = raw_input("What data type will be in the column? INTEGER, TEXT, NULL, REAL, BLOB  ")		
			a.add_column(table, column, datatype)
		elif choice == "2":
			table = raw_input("Which table do you want to query?  ")
			column = raw_input("Which column do you want to look at?  ")
			field = raw_input("what value are you looking for?  ")
			b.query(table, column, field)
		elif choice == "3":
			b.randomise()
		elif choice == "4":
			b.ingredients_search()
		elif choice == "0":
			program_running = False		
		else:
			print "Was that an option? NO!" 			

run_program()






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
	














"""
