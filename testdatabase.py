import sqlite3 as db
import sqlite3

def createdb():
    conn = sqlite3.connect("pptest.db")
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS user (sname text,gname text,sprovince text,gprovince text,tracking text)')
    conn.commit()
    conn.close()
