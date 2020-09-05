import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

def viewAll():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=%s OR author=%s OR year=%s OR isbn-%s",(title, author, year, isbn))
    rows = cur.fetchall() #This fetches all the values from the database, must be used for printing values. Dont have to commit the database in this case as nothing is being written by it  
    conn.close()
    return rows

def addEntry(title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)" , (title, author, year, isbn)) #ID in the database when assigned NULL get automatically updated by python
    conn.commit()
    conn.close()

connect()
addEntry("Half Girlfriend", "Chetan Bhagat", 2012, 1001)
print(viewAll())
