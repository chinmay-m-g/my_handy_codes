import sqlite3

# Connect to a Data base
conn = sqlite3.connect("database_1.sqlite")

# Create a Cursor
curr = conn.cursor()

# Create a table Executing a sql create statement
curr.execute(
    """ CREATE TABLE IF NOT EXISTS customer (
                    first_name TEXT,
                    last_name TEXT,
                    email_address TEXT
                )"""
)
# Data Types in SQLite
# 1. NULL
# 2. INTEGER
# 3. REAL
# 4. TEXT
# 5. BLOB


# Add a Single Entry into the database Executing a sql statement
curr.execute("INSERT INTO customer VALUES ('Sachin', 'Tendulkar', 'sachin@india.com')")

# Add multiple Entries
multiple_entries = [
    ("Mitchel", "Johnson", "mitchel@australia.com"),
    ("Virat", "Kohli", "virat@india.com"),
    ("Shane", "Warne", "shane@australia.com"),
]
curr.executemany("INSERT INTO customer VALUES (?,?,?)", multiple_entries)

# Commit the database
conn.commit()

# Close the database
conn.close()
