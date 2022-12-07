import sqlite3

# Connect to a Data base
conn = sqlite3.connect("database_1.sqlite")

# Create a Cursor
curr = conn.cursor()

# Add a Single Entry into the database Executing a sql statement
curr.execute("INSERT INTO customer VALUES ('first1', 'last1', 'first1@country.com')")
conn.commit()
curr.execute("INSERT INTO customer VALUES ('first2', 'last2', 'first2@country.com')")
conn.commit()
curr.execute("INSERT INTO customer VALUES ('first3', 'last3', 'first3@country.com')")
conn.commit()

# VIEW the DATABASE
curr.execute("SELECT * FROM customer")
filtered_values = curr.fetchall()

for filter_value in filtered_values:
    print(filter_value)

print("*" * 50)

# Deleting the row which we don't want
curr.execute("DELETE FROM customer WHERE first_name = 'first'")
conn.commit()

# VIEW the DATABASE
curr.execute("SELECT * FROM customer")
filtered_values = curr.fetchall()

for filter_value in filtered_values:
    print(filter_value)

print("*" * 50)

# Deleting the row using rowid
curr.execute("DELETE FROM customer WHERE rowid>=5")
conn.commit()

# VIEW the DATABASE
curr.execute("SELECT * FROM customer")
filtered_values = curr.fetchall()

for filter_value in filtered_values:
    print(filter_value)

# Commit the database
conn.commit()

# Close the database
conn.close()
