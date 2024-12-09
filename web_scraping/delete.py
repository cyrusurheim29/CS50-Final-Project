import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('volopps.db')
cursor = conn.cursor()

# SQL query to delete rows except the first two
delete_query = "DELETE FROM volunteer_opportunities WHERE ROWID > 2;"

# Execute the query
cursor.execute(delete_query)

# Commit the changes and close the connection
conn.commit()
conn.close()
