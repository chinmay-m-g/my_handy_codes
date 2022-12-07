import sqlite3

# Connect to a Data base
conn = sqlite3.connect("database_1.sqlite")

# Create a Cursor
curr = conn.cursor()

# Query the database without AND/OR
curr.execute(
    """SELECT rowid, * FROM customer 
    WHERE email_address LIKE '%india.com' and first_name='Saurav' or rowid >= 3
    ORDER BY last_name DESC
    LIMIT 4"""
)
for val in curr.fetchall():
    print(val)

# Commit the database
conn.commit()

# Close the database
conn.close()
