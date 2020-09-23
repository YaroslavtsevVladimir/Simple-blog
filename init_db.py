import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cursor = connection.cursor()

cursor.execute(
    'INSERT INTO posts (title, content) VALUES (?, ?)',
    ('First Post', 'Cool content for the first post')
)

cursor.execute(
    'INSERT INTO posts (title, content) VALUES (?, ?)',
    ('Secnond post', 'Not so cool content for the second blog')
)

connection.commit()
connection.close()
