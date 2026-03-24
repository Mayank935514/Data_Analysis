import sqlite3 

DB_file = 'example.db'
conn = sqlite3.connect(DB_file)
cursor = conn.cursor()

cursor.execute("INSERT INTO users (name, email) VALUES ('Bob', 'bob@example.com')")
conn.commit()

print('User inserted successfully.')
conn.close()