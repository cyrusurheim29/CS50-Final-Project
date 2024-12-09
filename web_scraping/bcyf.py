import pandas as pd
import sqlite3

a = open("bcyf_links.txt", "r")
lines = a.readlines()
links = []
for line in lines:
    links.append(line.replace("\n", ""))

# Load the CSV file
file_path = 'community_centers.csv'
df = pd.read_csv(file_path)

# Clean up column names (if necessary)
df.columns = df.columns.str.strip()
# Verify and transform DataFrame
if 'SITE' in df.columns and 'STREET' in df.columns:
    new_df = pd.DataFrame()
    new_df['name'] = df['SITE'] + " Center for Youth and Families"
    new_df['address'] = df['STREET'].astype(str).fillna('') + " Boston, MA, 0" + df['ZIP'].astype(str).fillna('')
    new_df['webpage'] = links  # Links from web scraping
    new_df['classification'] = "Boston Community Center"
else:
    raise ValueError("Expected columns 'SITE' and 'STREET' not found in the CSV file.")
# Connect to SQLite database (or other databases, e.g., PostgreSQL, MySQL)
connection = sqlite3.connect('volopps.db')  
for index, row in new_df.iterrows():
    new_df.at[index, 'address'] = row['address'].replace(".0", "")


# Define the table schema
table_name = 'volunteer_opportunities'
create_table_query = f"""
CREATE TABLE IF NOT EXISTS {table_name} (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    website TEXT,
    classification TEXT
);
"""

# Create the table
with connection:
    connection.execute(create_table_query)

# Insert the DataFrame into the table
new_df.to_sql(table_name, connection, if_exists='append', index=False)

# Verify the contents of the table
query_result = pd.read_sql(f"SELECT * FROM {table_name};", connection)
print(query_result)

# Close the connection
connection.close()
