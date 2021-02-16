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

        c.execute ('''SELECT * FROM users''')
        result = c.fetchall()
        for x in result:
            print(x)

    except sqlite3.Error as e:
        print('Failed to insert : ',e)
    finally :

        if conn:
            conn.close()

insertousers('ploypink','Rungphisitchai','ployp@kkumail.com','female')
insertousers('boat','wichianpan','chonlasit.w@kkumail.com','male')

