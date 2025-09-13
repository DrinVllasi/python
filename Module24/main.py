import sqlite3

connection = sqlite3.connect("example.db")

cursor = connection.cursor()

cursor.execute('''
  CREATE TABLE employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  
    name TEXT NOT NULL,
    position TEXT NOT NULL,
    department TEXT NOT NULL,
    salary REAL
)'''
)

connection.commit()