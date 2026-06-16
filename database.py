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

# Run query
cursor.execute(sql)

# Save changes and close connection
connection.commit()
connection.close()

print("Table was created successfully.")