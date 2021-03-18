import sqlite3 as db
import sqlite3

ntrack = []
i = 0
def index():
    print('ขนส่งของพวยพิ้งและโบ๊ทๆ')
    print('[1] เพิ่มพัสดุ\n[2] อัพเดทพัสดุ\n[3] เช็คเลขแทร็กกิ้ง\n[x] ออกจากโปรแกรม')

def add():
    sname = input('ชื่อผู้ส่งพัสดุ :')
    gname = input('ชื่อผู้รับพัสดุ :')
    stype = input('รูปแบบการส่ง\n[1] ส่งด่วน EMS\n[2] ส่งธรรมดา REG\nเลือกรูปแบบที่ต้องการส่ง : ')
    if stype == '1':
        print('สาขาปลายทาง\n[3] เลย\n[4] กรุงเทพ\n[5] ร้อยเอ็ด')
        global kk
        kk = int(input('เลือกสาขาปลายทาง : '))
        if kk == 3:
            priceems()
            emstracking()
            conn = sqlite3.connect("ppshipping.db")
            c = conn.cursor()
            c.execute('INSERT INTO user (sname,gname,sprovince,gprovince,tracking) values (?,?,?,?,?)',(sname,gname,'khonkaen','Loei',str(etrack)))
            conn.commit()
            conn.close()
        elif kk == 4:
            priceems()
            emstracking()
            conn = sqlite3.connect("ppshipping.db")
            c = conn.cursor()
            c.execute('INSERT INTO user (sname,gname,sprovince,gprovince,tracking) values (?,?,?,?,?)',(sname,gname,'khonkaen','bangkok',str(etrack)))
            conn.commit()
            conn.close()
        elif kk == 5:
            priceems()
            emstracking()
            conn = sqlite3.connect("ppshipping.db")
            c = conn.cursor()
            c.execute('INSERT INTO user (sname,gname,sprovince,gprovince,tracking) values (?,?,?,?,?)',(sname,gname,'khonkaen','Roiet',str(etrack)))
            conn.commit()
            conn.close()

    else:
        print('สาขาปลายทาง\n[3] เลย\n[4] กรุงเทพ\n[5] ร้อยเอ็ด')
        kk = int(input('เลือกสาขาปลายทาง : '))
        if kk == 3:
            pricereg()
            regtracking()
            conn = sqlite3.connect("ppshipping.db")
            c = conn.cursor()
            c.execute('INSERT INTO user (sname,gname,sprovince,gprovince,tracking) values (?,?,?,?,?)',(sname,gname,'khonkaen','Loei',str(rtrack)))
            conn.commit()
            conn.close()
        elif kk == 4:
            pricereg()
            regtracking()
            conn = sqlite3.connect("ppshipping.db")
            c = conn.cursor()
            c.execute('INSERT INTO user (sname,gname,sprovince,gprovince,tracking) values (?,?,?,?,?)',(sname,gname,'khonkaen','bangkok',str(rtrack)))
            conn.commit()
            conn.close()

def createdb():
    conn = sqlite3.connect("loeishipping.db")
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS user (deliver name text,Receive name text,get address text,khonkaen text,Nong Bua Lamphu text,station)')
    conn.commit()
    conn.close()

def priceems():
    priceems =float(input('weight of package (kg) :'))
    if priceems <= 1 :
        Totalems = (priceems + 30) + (7*kk)
    elif 1 < priceems <= 10 :
        Totalems = (priceems + 60) + (7*kk)
    else:
        Totalems = (priceems + 100) + (7*kk)
    print(str(int(Totalems)+1) +' baht')

def pricereg():
    priceems =float(input('weight of package (kg) :'))
    if priceems <= 1 :
        Totalems = (priceems + 15) + (7*kk)
    elif 1 < priceems <= 10 :
        Totalems = (priceems + 15) + (7*kk)
    else:
        Totalems = (priceems + 50) + (7*kk)
    print(str(int(Totalems)+1) +' baht')

def emstracking():
    import random
    global etrack
    for i in range(10):
        atrack = (random.randint(0,9))
        ntrack.append(atrack)
    a=0
    b=1
    for i in range(10):
        a=a+(ntrack[i]*(b))
        b=b*10
    etrack = 'EMS' + str(a) + 'TH'
    print(etrack)

def regtracking():
    global rtrack
    import random
    for i in range(10):
        atrack = (random.randint(0,9))
        ntrack.append(atrack)
    a=0
    b=1
    for i in range(10):
        a=a+(ntrack[i]*(b))
        b=b*10
    rtrack = 'REG' + str(a) + 'TH'
    print(rtrack)

#finalprogram
#createdb()
while True:
    index()
    choose = input('choose menu : ')
    if choose == '1':
        add()
        break
    elif choose == '2':
        print('Tracking number\tsend name\tget name\tsend province\tget province')
        conn = sqlite3.connect("ppshipping.db")
        c = conn.cursor()
        c.execute ('''SELECT * FROM user''')
        result = c.fetchall()
        for x in result:
            info_tracking = str(x[4])
            info_sname = str(x[0])
            info_gname = str(x[1])
            info_sprovince = str(x[2])
            info_gprovince = str(x[3])
            print(info_tracking+ '\t' + info_sname + '\t' + info_gname + '\t' + info_sprovince + '\t' + info_gprovince)