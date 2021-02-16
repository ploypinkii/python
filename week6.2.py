'''

#การเพิ่มข้อมูลแบบใช้ดาต้า (เอาไว้ใช้ในการอินพุต)
import sqlite3
def insertousers (fname,lname,email,sex):
    try:
        conn = sqlite3.connect(r'D:\ED\term2\ED251007\ploychomphu_python\week6.db')
        c = conn.cursor()

        sql = ''' INSERT INTO users (fname,lname,email,sex) VALUES (?,?,?,?) '''
        data = ('A','A','A','A')
        c.execute('INSERT INTO users (fname,lname,email,sex) VALUES (?,?,?,?)',data)
        conn.commit()
        c.close()

    except sqlite3.Error as e:
        print('Failed to insert : ',e)
    finally :

        if conn:
            conn.close()

insertousers('ploypink','Rungphisitchai','ployp@kkumail.com','female')
insertousers('boat','wichianpan','chonlasit.w@kkumail.com','male')


#การเพิ่มข้อมูลหลายๆข้อมูล
import sqlite3
def insertousers (fname,lname,email,sex):
    try:
        conn = sqlite3.connect(r'D:\ED\term2\ED251007\ploychomphu_python\week6.db')
        c = conn.cursor()

        sql = ''' INSERT INTO users (fname,lname,email,sex) VALUES (?,?,?,?) '''
        data = ('A','A','A','A'),('B','B','B','B')
        c.executemany('INSERT INTO users (fname,lname,email,sex) VALUES (?,?,?,?)',data)
        conn.commit()
        c.close()

    except sqlite3.Error as e:
        print('Failed to insert : ',e)
    finally :

        if conn:
            conn.close()

insertousers('ploypink','Rungphisitchai','ployp@kkumail.com','female')
insertousers('boat','wichianpan','chonlasit.w@kkumail.com','male')

#การแสดงเฉพาะตัวที่คีย์ข้อมูล
import sqlite3
conn = sqlite3.connect(r'D:\ED\term2\ED251007\ploychomphu_python\week6.db')
c = conn.cursor()

add = input('Enter name :')
name = (add,)
c.execute ('SELECT * FROM users WHERE fname = ?',name)
result = c.fetchall()
for x in result:
    print(x)

#การแสดงจากมากไปหาน้อย
import sqlite3
conn = sqlite3.connect(r'D:\ED\term2\ED251007\ploychomphu_python\week6.db')
c = conn.cursor()

c.execute ('SELECT * FROM users ORDER BY id DESC')
result = c.fetchall()
for x in result:
    print(x)

#การแสดงข้อมูลแบบบอกตำแหน่งเริ่มต้นและแสดงจำนวนเท่าไหร่
import sqlite3
conn = sqlite3.connect(r'D:\ED\term2\ED251007\ploychomphu_python\week6.db')
c = conn.cursor()

c.execute ('SELECT * FROM users LIMIT 5 OFFSET 2')
result = c.fetchall()
for x in result:
    print(x)

#การลบข้อมูลเฉพาะเจาะจง
import sqlite3
conn = sqlite3.connect(r'D:\ED\term2\ED251007\ploychomphu_python\week6.db')
c = conn.cursor()
add = input('Enter ID to delete : ')
name = (add,)
c.execute ('DELETE FROM users WHERE id = ?',name)


#การลบข้อมูลทั้งหมด
import sqlite3
conn = sqlite3.connect(r'D:\ED\term2\ED251007\ploychomphu_python\week6.db')
c = conn.cursor()
c.execute ('DELETE FROM users')
conn.commit()
c.close()
'''
import sqlite3
conn = sqlite3.connect(r'D:\ED\term2\ED251007\ploychomphu_python\week6.db')
c = conn.cursor()
c.execute ()
conn.commit()
c.close()

c.execute ('''SELECT * FROM users''')
result = c.fetchall()
for x in result:
    print(x)