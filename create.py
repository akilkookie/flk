import sqlite3

connection = sqlite3.connect("user1.db")
cursor = connection.cursor()

command ="""CREATE TABLE IF NOT EXISTS users1(name TEXT, password TEXT)"""

cursor.execute(command)
# cursor.execute("INSERT INTO users VALUES('AKILA','akilkookie@1')")
# cursor.execute("INSERT INTO users VALUES('nithesh','jk@1')")
# cursor.execute("INSERT INTO users VALUES('jungkook','akilkookie')")

#connection.commit()