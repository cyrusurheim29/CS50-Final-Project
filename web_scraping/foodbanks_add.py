import pandas as pd
import sqlite3

table_name = "volunteer_opportunities"

connection = sqlite3.connect('volopps.db')

df = pd.read_csv('complete_kitchens3.csv')
# Insert the DataFrame into the table
df.to_sql(table_name, connection, if_exists='append', index=False)

# Verify the contents of the table
query_result = pd.read_sql(f"SELECT * FROM {table_name};", connection)
print(query_result)

# Close the connection
connection.close()