import sqlite3

# Connect to a Data base
conn = sqlite3.connect("database_1.sqlite")

# Create a Cursor
curr = conn.cursor()

# Query a table Executing a sql create statement
curr.execute("SELECT * FROM customer")
# one_data = curr.fetchone() # Returns only one entry in the database
# many_data = curr.fetchmany(2) # Returns the specified entries in the database
all_data = curr.fetchall()  # Returns all the database in the form of List of tuples

# print("one_data", one_data)
# print("many_data", many_data)
for each_data in all_data:
    print(each_data)

# Query along with rowid (rowid is a unique id which the sql saves)
curr.execute("SELECT rowid, * FROM customer")
all_data = curr.fetchall()
for one_data in all_data:
    print(one_data)


# Commit the database
conn.commit()

# Close the database
conn.close()
