import sqlite3

# Connect to a Data base
conn = sqlite3.connect("database_1.sqlite")

# Create a Cursor
curr = conn.cursor()

# Drop the Table
curr.execute("DROP TABLE IF EXISTS customer")

# Commit the database
conn.commit()

try:
    curr.execute("SELECT * FROM customer")
except sqlite3.OperationalError as err:
    print(str(err))
    if str(err) == "no such table: customer":
        print("Table DELETED")

# Close the database
conn.close()
