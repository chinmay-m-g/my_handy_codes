import sqlite3

# Connect to a Data base
conn = sqlite3.connect("database_1.sqlite")

# Create a Cursor
curr = conn.cursor()

# Selecting and ordering the data (ASC Stands for ascending order)
curr.execute("SELECT rowid, * from customer ORDER BY rowid ASC")

# VIEW the DATABASE
filtered_values = curr.fetchall()

for filter_value in filtered_values:
    print(filter_value)

print("*" * 50)

# Selecting and ordering the data (DESC stands for descending order)
curr.execute("SELECT rowid, * from customer ORDER BY rowid DESC")
# VIEW the DATABASE
filtered_values = curr.fetchall()

for filter_value in filtered_values:
    print(filter_value)

print("*" * 50)

# Filtering by last_name
curr.execute("SELECT rowid, * from customer ORDER BY last_name ASC")
# VIEW the DATABASE
filtered_values = curr.fetchall()

for filter_value in filtered_values:
    print(filter_value)


# Commit the database
conn.commit()

# Close the database
conn.close()
