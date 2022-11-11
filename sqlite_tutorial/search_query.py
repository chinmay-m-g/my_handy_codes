import sqlite3

# Connect to a Data base
conn = sqlite3.connect("database_1.sqlite")

# Create a Cursor
curr = conn.cursor()

# Search for a specific data Executing a sql Where statement
curr.execute("SELECT * FROM customer WHERE last_name = 'Tendulkar'")
filtered_values_1 = curr.fetchall()

for filter_value in filtered_values_1:
    print(filter_value)

print("*" * 50)
curr.execute("SELECT * FROM customer WHERE email_address LIKE '%@india.com'")
filtered_values_2 = curr.fetchall()

for filter_value in filtered_values_2:
    print(filter_value)

# Commit the database
conn.commit()

# Close the database
conn.close()
