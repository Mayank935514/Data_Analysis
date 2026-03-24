import sqlite3

# Name of the database file
DB_file = 'example.db'

# Connects to the database(creates the file if it doesn't exists)
conn = sqlite3.connect(DB_file)

# Create a cursor to execute SQL commands
cursor = conn.cursor()

# Create a users table if it doesn't exists
cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
            ''')

# Save the commit(changes) to the database
conn.commit()

# Print a message to shoe that the table is created 
print("Table created successfully")

# Close the connection to the database
conn.close()