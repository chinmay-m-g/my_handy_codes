import sqlite3

# Connect to a Data base
conn = sqlite3.connect("database_1.sqlite")

# Create a Cursor
curr = conn.cursor()

# Update a table Executing a sql UPDATE statement
curr.execute(
    """ UPDATE customer SET last_name='Starc'
        WHERE first_name='Mitchel'"""
)
# Commit the database
conn.commit()

# View the data base
curr.execute("SELECT * FROM customer")
values = curr.fetchall()
for value in values:
    print(value)

print("*" * 50)

# Update based on the rowid (Preferred)
curr.execute(
    """ UPDATE customer SET 
            first_name = "Saurav", 
            last_name='Ganguly', 
            email_address ='saurav@india.com'
        WHERE rowid = 1"""
)

# Commit the database
conn.commit()

# View the data base
curr.execute("SELECT * FROM customer")
values = curr.fetchall()
for value in values:
    print(value)


# Close the database
conn.close()
