import sqlite3

db = 'recipe_db.sqlite'    # name of the sqlite database file
table_name1 = 'recipes'  # name of the table to be created
new_field = 'title' # name of the column
field_type = 'VARCHAR(20)'  # column data type

# Connecting to the database file
conn = sqlite3.connect(db)
c = conn.cursor()

# Creating a new SQLite table with 1 column
c.execute('CREATE TABLE {tn} ({nf} {ft})'\
        .format(tn=table_name1, nf=new_field, ft=field_type))


# Committing changes and closing the connection to the database file
conn.commit()
conn.close()