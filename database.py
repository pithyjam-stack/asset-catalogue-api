import sqlite3

# Connect to the database
connection = sqlite3.connect("asset_catalogue.db")

# Create cursor object to execute SQL commands
cursor = connection.cursor()

# CREATE TABLE query
sql = """
CREATE TABLE IF NOT EXISTS assets(
    asset_id INTEGER PRIMARY KEY AUTOINCREMENT,
    version_num INTEGER NOT NULL,

    asset_name TEXT NOT NULL,
    asset_type TEXT NOT NULL,
    project TEXT NOT NULL,
    description TEXT NOT NULL
)
"""

insert = """
INSERT INTO assets ( 
version_num,
asset_name, 
asset_type, 
project, 
description)

VALUES(
1,
'Forest_ambience.wav',
'audio',
'Horror Game',
'Forest ambience loop'
)
"""

select_from = """
SELECT * FROM assets;
"""

clear_table = """
DELETE FROM assets;
"""

# Run query
cursor.execute(clear_table)
cursor.execute(sql)
cursor.execute(insert)
cursor.execute(select_from)
rows = cursor.fetchall()

for row in rows:
    print(f"{row[0]} : {row[1]} : {row[2]} : {row[3]} : {row[4]} : {row[5]}")

# Save changes and close connection
connection.commit()
connection.close()

print("Table was created successfully.")