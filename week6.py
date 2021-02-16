import sqlite3
conn = sqlite3.connect(r'D:\ED\term2\ED251007\ploychomphu_python\week6.db')
c = conn.cursor()
c.execute('''CREATE TABLE users (id integer PRIMARY KEY AUTOINCREMENT,
    fname varchar(30) NOT NULL,
    laname varchar(30) NOT NULL,
    email varchhar(100) NOT NULL)''')
c.execute('''INSERT INTO users (id,fname,lname,email) VALUES (NULL,'A','A','A')''')
conn.commit()
conn.close()
