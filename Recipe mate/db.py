import sqlite3

db = 'recipe_db.sqlite' 

def add_column(table, column, datatype):
	conn = sqlite3.connect(db)
	c = conn.cursor()

	c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
	        .format(tn=table, cn=column, ct=datatype))

	conn.commit()
	conn.close()

def set_mode():
	choice = raw_input("What do you want to do. Type 1 to add a column to an existing table:  ")
	if choice == "1":
		table = raw_input("Which table?  ")
		column = raw_input("What's the column name?  ")
		datatype = raw_input("What data type will be in the column? INTEGER, TEXT, NULL, REAL, BLOB  ")
		add_column(table, column, datatype)
	else:
		print "Was that an option? NO!"

set_mode()
"""
sqlite_file = 'my_first_db.sqlite'    # name of the sqlite database file
table_name = 'my_table_2'   # name of the table to be created
id_column = 'my_1st_column' # name of the PRIMARY KEY column
new_column1 = 'my_2nd_column'  # name of the new column
new_column2 = 'my_3nd_column'  # name of the new column
column_type = 'TEXT' # E.g., INTEGER, TEXT, NULL, REAL, BLOB
default_val = 'Hello World' # a default value for the new column rows

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# A) Adding a new column without a row value
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name, cn=new_column1, ct=column_type))

# B) Adding a new column with a default row value
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct} DEFAULT '{df}'"\
        .format(tn=table_name, cn=new_column2, ct=column_type, df=default_val))

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()
"""