import sqlite3

# Connect to a Data base
conn = sqlite3.connect("database_1.sqlite")

# Create a Cursor
curr = conn.cursor()

# Query the database without AND/OR
curr.execute("SELECT rowid, * FROM customer WHERE email_address LIKE '%india.com'")
for val in curr.fetchall():
    print(val)
print("*" * 50)

# Query the database using AND
curr.execute(
    "SELECT rowid, * FROM customer WHERE email_address LIKE '%india.com' and first_name='Saurav'"
)
for val in curr.fetchall():
    print(val)
print("*" * 50)

# Query the database using OR
curr.execute(
    "SELECT rowid, * FROM customer WHERE email_address LIKE '%india.com' or rowid>=3"
)
for val in curr.fetchall():
    print(val)

# Commit the database
conn.commit()

# Close the database
conn.close()
