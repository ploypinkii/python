import sqlite3 as db
import sqlite3
conn = sqlite3.connect(r"D:\ED\term2\ED251007\ploychomphu_python\shipping.db")
c = conn.cursor()
global shipto
ntrack = []

def createdb():
    conn = sqlite3.connect("shipping.db")
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS loei (tracking text,khonkaen text,nongbua lamphu text,loei text, deliver name text,receive name text,address text)')
    c.execute('CREATE TABLE IF NOT EXISTS surin (tracking text,khonkaen text,maha sarakham text,roiet text,surin text,deliver name text,receive name text,address text)')
    c.execute('CREATE TABLE IF NOT EXISTS bangkok (tracking text,khonkaen text,nakorn ratchasima text,saraburi text,bangkok text,deliver name text,receive name text,address text)')
    conn.commit()
    conn.close()
    
def index():
    print('********************\nQuix Express\n********************')
    print('[1] add package\n[2] update package\n[3] checking track\n[x] exit')

def priceems():
    priceems =float(input('weight of package (kg) :'))
    if priceems <= 1 :
        Totalems = (priceems + 30) + (7*shipto)
    elif 1 < priceems <= 10 :
        Totalems = (priceems + 60) + (7*shipto)
    else:
        Totalems = (priceems + 100) + (7*shipto)
    ftotalems = str(int(Totalems)+1)
    print('\nTotal\t\t'+ftotalems +' baht')

def qixtrackingbkk():
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
    etrack = 'QIX' + str(a) + 'BKK'
    str(etrack)
    print('tracking number\t'+etrack)

def qixtrackingsru():
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
    etrack = 'QIX' + str(a) + 'SRU'
    str(etrack)
    print('tracking number\t'+etrack)

def qixtrackingloe():
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
    etrack = 'QIX' + str(a) + 'LOE'
    str(etrack)
    print('tracking number\t'+etrack)

def pricereg():
    shipto = int(input('\nDeliver to\n[4] Bangkok\n[5] Loei\n[6] Surin\n\nEnter your choice : '))
    if shipto == 4:
        priceems =float(input('weight of package (kg) :'))
        if priceems <= 1 :
            Totalems = (priceems + 15) + (7*shipto)
        elif 1 < priceems <= 10 :
            Totalems = (priceems + 15) + (7*shipto)
        else:
            Totalems = (priceems + 50) + (7*shipto)
        ftotalems = str(int(Totalems)+1)
        print('\nTotal\t\t'+ftotalems +' baht')
    elif shipto == 5:
        priceems =float(input('weight of package (kg) :'))
        if priceems <= 1 :
            Totalems = (priceems + 15) + (7*shipto)
        elif 1 < priceems <= 10 :
            Totalems = (priceems + 15) + (7*shipto)
        else:
            Totalems = (priceems + 50) + (7*shipto)
        ftotalems = str(int(Totalems)+1)
        print('\nTotal\t\t'+ftotalems +' baht')
    elif shipto == 6:
        priceems =float(input('weight of package (kg) :'))
        if priceems <= 1 :
            Totalems = (priceems + 15) + (7*shipto)
        elif 1 < priceems <= 10 :
            Totalems = (priceems + 15) + (7*shipto)
        else:
            Totalems = (priceems + 50) + (7*shipto)
        ftotalems = str(int(Totalems)+1)
        print('\nTotal\t\t'+ftotalems +' baht')

def regtrackingbkk():
    import random
    global rtrack
    for i in range(10):
        atrack = (random.randint(0,9))
        ntrack.append(atrack)
    a=0
    b=1
    for i in range(10):
        a=a+(ntrack[i]*(b))
        b=b*10
    rtrack = 'NOR' + str(a) + 'BKK'
    print('tracking number\t'+rtrack)

def regtrackingloe():
    import random
    global rtrack
    for i in range(10):
        atrack = (random.randint(0,9))
        ntrack.append(atrack)
    a=0
    b=1
    for i in range(10):
        a=a+(ntrack[i]*(b))
        b=b*10
    rtrack = 'NOR' + str(a) + 'LOE'
    print('tracking number\t'+rtrack)

def regtrackingsru():
    import random
    global rtrack
    for i in range(10):
        atrack = (random.randint(0,9))
        ntrack.append(atrack)
    a=0
    b=1
    for i in range(10):
        a=a+(ntrack[i]*(b))
        b=b*10
    rtrack = 'NOR' + str(a) + 'SUR'
    print('tracking number\t'+rtrack)

def add():
    dname = input('Enter your deliver name : ')
    rname = input('Enter your recive name : ')
    aname = input('Enter address of recieve : ')
    shipto = int(input('\nDeliver to\n[4] Bangkok\n[5] Loei\n[6] Surin\n\nEnter your choice : '))
    if shipto == 4:
        stype = input('\nkind of shipping\n[1] QIX\n[2] NOR\n\nEnter your type : ')
        if stype == '1':
            priceems =float(input('weight of package (kg) :'))
            if priceems <= 1 :
                Totalems = (priceems + 30) + (7*shipto)
            elif 1 < priceems <= 10 :
                Totalems = (priceems + 60) + (7*shipto)
            else:
                Totalems = (priceems + 100) + (7*shipto)
            ftotalems = str(int(Totalems)+1)
            print('\nTotal\t\t'+ftotalems +' baht')
            #สิ้นสุดการคำนวณราคาที่นี่
            qixtrackingbkk()
            c.execute('INSERT INTO bangkok (tracking,khonkaen,delivername,recivename,address,price,weight) values (?,?,?,?,?,?,?)',(str(etrack),'in system',dname,rname,aname,ftotalems,priceems))
            conn.commit()
            c.execute('INSERT INTO shippingcheck (type,Province,tracking,delivername,recivename,price,weight) values (?,?,?,?,?,?,?)',('QIX','BKK',str(etrack),dname,rname,ftotalems,priceems))
            conn.commit()

        elif stype == '2':
            pricereg =float(input('weight of package (kg) :'))
            if pricereg <= 1 :
                Totalreg = (pricereg + 15) + (7*shipto)
            elif 1 < pricereg <= 10 :
                Totalreg = (pricereg + 15) + (7*shipto)
            else:
                Totalreg = (pricereg + 50) + (7*shipto)
            ftotalreg = str(int(Totalreg)+1)
            print('\nTotal\t\t'+ftotalreg +' baht')
            #สิ้นสุดการคำนวณราคาที่นี่
            regtrackingbkk()
            c.execute('INSERT INTO bangkok (tracking,khonkaen,delivername,recivename,address,price,weight) values (?,?,?,?,?,?,?)',(str(rtrack),'in system',dname,rname,aname,ftotalreg,pricereg))
            conn.commit()
            c.execute('INSERT INTO shippingcheck (type,Province,tracking,delivername,recivename,price,weight) values (?,?,?,?,?,?,?)',('NOR','BKK',str(rtrack),dname,rname,ftotalreg,pricereg))
            conn.commit()
    if shipto == 5:
        stype = input('\nkind of shipping\n[1] QIX\n[2] NOR\n\nEnter your type : ')
        if stype == '1':
            priceems =float(input('weight of package (kg) :'))
            if priceems <= 1 :
                Totalems = (priceems + 30) + (7*shipto)
            elif 1 < priceems <= 10 :
                Totalems = (priceems + 60) + (7*shipto)
            else:
                Totalems = (priceems + 100) + (7*shipto)
            ftotalems = str(int(Totalems)+1)
            print('\nTotal\t\t'+ftotalems +' baht')
            #สิ้นสุดการคำนวณราคาที่นี่
            qixtrackingloe()
            c.execute('INSERT INTO loei (tracking,khonkaen,delivername,recivename,address,price,weight) values (?,?,?,?,?,?,?)',(str(etrack),'in system',dname,rname,aname,ftotalems,priceems))
            conn.commit()
            c.execute('INSERT INTO shippingcheck (type,Province,tracking,delivername,recivename,price,weight) values (?,?,?,?,?,?,?)',('QIX','LOE',str(etrack),dname,rname,ftotalems,priceems))
            conn.commit()

        elif stype == '2':
            pricereg =float(input('weight of package (kg) :'))
            if pricereg <= 1 :
                Totalreg = (pricereg + 15) + (7*shipto)
            elif 1 < pricereg <= 10 :
                Totalreg = (pricereg + 15) + (7*shipto)
            else:
                Totalreg = (pricereg + 50) + (7*shipto)
            ftotalreg = str(int(Totalreg)+1)
            print('\nTotal\t\t'+ftotalreg +' baht')
            #สิ้นสุดการคำนวณราคาที่นี่
            regtrackingloe()
            c.execute('INSERT INTO loei (tracking,khonkaen,delivername,recivename,address,price,weight) values (?,?,?,?,?,?,?)',(str(rtrack),'in system',dname,rname,aname,ftotalreg,pricereg))
            conn.commit()
            c.execute('INSERT INTO shippingcheck (type,Province,tracking,delivername,recivename,price,weight) values (?,?,?,?,?,?,?)',('NOR','LOE',str(rtrack),dname,rname,ftotalreg,pricereg))
            conn.commit()
    if shipto == 6:
        stype = input('\nkind of shipping\n[1] QIX\n[2] NORM\n\nEnter your type : ')
        if stype == '1':
            priceems =float(input('weight of package (kg) :'))
            if priceems <= 1 :
                Totalems = (priceems + 30) + (7*shipto)
            elif 1 < priceems <= 10 :
                Totalems = (priceems + 60) + (7*shipto)
            else:
                Totalems = (priceems + 100) + (7*shipto)
            ftotalems = str(int(Totalems)+1)
            print('\nTotal\t\t'+ftotalems +' baht')
            #สิ้นสุดการคำนวณราคาที่นี่
            qixtrackingsru()
            c.execute('INSERT INTO surin (tracking,khonkaen,delivername,recivename,address,price,weight) values (?,?,?,?,?,?,?)',(str(etrack),'in system',dname,rname,aname,ftotalems,priceems))
            conn.commit()
            c.execute('INSERT INTO shippingcheck (type,Province,tracking,delivername,recivename,price,weight) values (?,?,?,?,?,?,?)',('QIX','SRU',str(etrack),dname,rname,ftotalems,priceems))
            conn.commit()
        elif stype == '2':
            pricereg =float(input('weight of package (kg) :'))
            if pricereg <= 1 :
                Totalreg = (pricereg + 15) + (7*shipto)
            elif 1 < pricereg <= 10 :
                Totalreg = (pricereg + 15) + (7*shipto)
            else:
                Totalreg = (pricereg + 50) + (7*shipto)
            ftotalreg = str(int(Totalreg)+1)
            print('\nTotal\t\t'+ftotalreg +' baht')
            #สิ้นสุดการคำนวณราคาที่นี่
            regtrackingsru()
            c.execute('INSERT INTO surin (tracking,khonkaen,delivername,recivename,address,price,weight) values (?,?,?,?,?,?,?)',(str(rtrack),'in system',dname,rname,aname,ftotalreg,pricereg))
            conn.commit()
            c.execute('INSERT INTO shippingcheck (type,Province,tracking,delivername,recivename,price,weight) values (?,?,?,?,?,?,?)',('NOR','SRU',str(rtrack),dname,rname,ftotalreg,pricereg))
            conn.commit()

def register():
    try:
        username = input('Enter new username : ')
        password = input('Enter new password : ')
        c.execute('INSERT INTO login(username,password) VALUES(?,?)',(username,password))
    except:
        print('Username already used please Enter again')
    conn.commit()

def login():
    try:
        verusername = input('Enter Username : ')
        vuser = [verusername,]
        verpassword = input('Enter password : ')
        vpassword = [verpassword,]
        c.execute('SELECT * FROM login WHERE username = ?',vuser)
        c.execute('SELECT * FROM login WHERE password = ?',vpassword)
        result = c.fetchone()
        if verusername == result[0] and verpassword == result[1]:
            print('successful!')
        else:
            print('username or password are incorrect please try again!')

    except:
        print('ไม่มีชื่อผู้ใช้นี้ในระบบ กรุณาลองใหม่')
    conn.commit()

def update():
    global strack
    strack = input('Enter Tracking : ')
    strack = [strack,]
    c.execute('SELECT * FROM  shippingcheck WHERE tracking = ?',strack)
    result = c.fetchone()
    #print(result[1])
    if result[1] == 'BKK':
        while True:
            up = str(input('[1] khonkaen\n[2] nakorn ratchasima\n[3] saraburi\n[4] bangkok\n[5] back\nEnter your choice : '))
            if up == '1':
                ch = str(input('[a] -\n[b] pass this station\n[c] send success!\nEnter your number : '))
                if ch == 'a' :
                    c.execute('UPDATE bangkok SET khonkaen = "-" WHERE tracking = ?',strack)
                    conn.commit()
                elif ch == 'b':
                    c.execute('UPDATE bangkok SET khonkaen = "pass this station" WHERE tracking = ?',strack)
                    conn.commit()
                elif ch == 'c':
                    c.execute('UPDATE bangkok SET khonkaen = "send success!" WHERE tracking = ?',strack)
                    conn.commit()
            elif up == '2':
                ch = str(input('[a] -\n[b] pass this station\n[c] send success!\nEnter your number : '))
                if ch == 'a' :
                    c.execute('UPDATE bangkok SET nakornrachasima = "-" WHERE tracking = ?',strack)
                    conn.commit()
                elif ch == 'b':
                    c.execute('UPDATE bangkok SET nakornrachasima = "pass this station" WHERE tracking = ?',strack)
                    conn.commit()
                elif ch == 'c':
                    c.execute('UPDATE bangkok SET nakornrachasima = "send success!" WHERE tracking = ?',strack)
                    conn.commit()
            elif up == '3':
                ch = str(input('[a] -\n[b] pass this station\n[c] send success!\nEnter your number : '))
                if ch == 'a' :
                    c.execute('UPDATE bangkok SET saraburi = "-" WHERE tracking = ?',strack)
                    conn.commit()
                elif ch == 'b':
                    c.execute('UPDATE bangkok SET saraburi = "pass this station" WHERE tracking = ?',strack)
                    conn.commit()
                elif ch == 'c':
                    c.execute('UPDATE bangkok SET saraburi = "send success!" WHERE tracking = ?',strack)
                    conn.commit()
            elif up == '4':
                ch = str(input('[a] -\n[b] pass this station\n[c] send success!\nEnter your number : '))
                if ch == 'a' :
                    c.execute('UPDATE bangkok SET bangkok = "-" WHERE tracking = ?',strack)
                    conn.commit()
                elif ch == 'b':
                    c.execute('UPDATE bangkok SET bangkok = "pass this station" WHERE tracking = ?',strack)
                    conn.commit()
                elif ch == 'c':
                    c.execute('UPDATE bangkok SET bangkok = "send success!" WHERE tracking = ?',strack)
                    conn.commit()
            elif up == '5':
                break
    elif result[1] == 'SRU':
        while True:
            up = str(input('[1] khonkaen\n[2] mahasarakham\n[3] roiet\n[4] surin\n[5] back\nEnter your choice : '))
            if up == '1':
                ch = str(input('[a] -\n[b] pass this station\n[c] send success!\nEnter your number : '))
                if ch == 'a' :
                    c.execute('UPDATE surin SET khonkaen = "-" WHERE tracking = ?',strack)
                    conn.commit()
                elif ch == 'b':
                    c.execute('UPDATE surin SET khonkaen = "pass this station" WHERE tracking = ?',strack)
                    conn.commit()
                elif ch == 'c':
                    c.execute('UPDATE surin SET khonkaen = "send success!" WHERE tracking = ?',strack)
                    conn.commit()
            elif up == '2':
                ch = str(input('[a] -\n[b] pass this station\n[c] send success!\nEnter your number : '))
                if ch == 'a' :
                    c.execute('UPDATE surin SET mahasarakham = "-" WHERE tracking = ?',strack)
                    conn.commit()
                elif ch == 'b':
                    c.execute('UPDATE surin SET mahasarakham = "pass this station" WHERE tracking = ?',strack)
                    conn.commit()
                elif ch == 'c':
                    c.execute('UPDATE surin SET mahasarakham = "send success!" WHERE tracking = ?',strack)
                    conn.commit()
            elif up == '3':
                ch = str(input('[a] -\n[b] pass this station\n[c] send success!\nEnter your number : '))
                if ch == 'a' :
                    c.execute('UPDATE surin SET roiet = "-" WHERE tracking = ?',strack)
                    conn.commit()
                elif ch == 'b':
                    c.execute('UPDATE surin SET roiet = "pass this station" WHERE tracking = ?',strack)
                    conn.commit()
                elif ch == 'c':
                    c.execute('UPDATE surin SET roiet = "send success!" WHERE tracking = ?',strack)
                    conn.commit()
            elif up == '4':
                ch = str(input('[a] -\n[b] pass this station\n[c] send success!\nEnter your number : '))
                if ch == 'a' :
                    c.execute('UPDATE surin SET surin = "-" WHERE tracking = ?',strack)
                    conn.commit()
                elif ch == 'b':
                    c.execute('UPDATE surin SET surin = "pass this station" WHERE tracking = ?',strack)
                    conn.commit()
                elif ch == 'c':
                    c.execute('UPDATE surin SET surin = "send success!" WHERE tracking = ?',strack)
                    conn.commit()
            elif up == '5':
                break
    elif result[1] == 'LOE':
        while True:
            up = str(input('[1] khonkaen\n[2] nongbualamphu\n[3] loei\n[4] back\nEnter your choice : '))
            if up == '1':
                ch = str(input('[a] -\n[b] pass this station\n[c] send success!\nEnter your number : '))
                if ch == 'a' :
                    c.execute('UPDATE loei SET khonkaen = "-" WHERE tracking = ?',strack)
                    conn.commit()
                elif ch == 'b':
                    c.execute('UPDATE loei SET khonkaen = "pass this station" WHERE tracking = ?',strack)
                    conn.commit()
                elif ch == 'c':
                    c.execute('UPDATE loei SET khonkaen = "send success!" WHERE tracking = ?',strack)
                    conn.commit()
            elif up == '2':
                ch = str(input('[a] -\n[b] pass this station\n[c] send success!\nEnter your number : '))
                if ch == 'a' :
                    c.execute('UPDATE surin SET nongbualamphu = "-" WHERE tracking = ?',strack)
                    conn.commit()
                elif ch == 'b':
                    c.execute('UPDATE loei SET nongbualamphu = "pass this station" WHERE tracking = ?',strack)
                    conn.commit()
                elif ch == 'c':
                    c.execute('UPDATE loei SET nongbualamphu = "send success!" WHERE tracking = ?',strack)
                    conn.commit()
            elif up == '3':
                ch = str(input('[a] -\n[b] pass this station\n[c] send success!\nEnter your number : '))
                if ch == 'a' :
                    c.execute('UPDATE loei SET loei = "-" WHERE tracking = ?',strack)
                    conn.commit()
                elif ch == 'b':
                    c.execute('UPDATE loei SET loei = "pass this station" WHERE tracking = ?',strack)
                    conn.commit()
                elif ch == 'c':
                    c.execute('UPDATE loei SET loei = "send success!" WHERE tracking = ?',strack)
                    conn.commit()
            elif up == '4':
                break
        
def checking():
    global search
    search = input('Enter Trackingnumber : ')
    search = [search,]
    c.execute('SELECT * FROM  shippingcheck WHERE tracking = ?',search)
    result = c.fetchone()
    if result[1] == 'BKK':
        c.execute('SELECT * FROM bangkok WHERE tracking = ?',search)
        conn.commit()
        result = c.fetchone()
        print(str(result[0])+'  '+str(result[1])+'  '+str(result[2])+'  '+str(result[3])+'  '+str(result[4])+'  '+str(result[5])+'  '+str(result[6])+'  '+str(result[7])+'  '+str(result[8])+'  '+str(result[9]))
        #       เลขแทร็ก             ขอนแก่น             นครราชสีมา            สระบุรี               กรุงเทพ              ชื่อคนส่ง              ชื่อคนรับ              ที่อยู่                 ราคา                น้ำหนัก
    if result[1] == 'SRU':
        c.execute('SELECT * FROM surin WHERE tracking = ?',search)
        conn.commit()
        result = c.fetchone()
        print(str(result[0])+'  '+str(result[1])+'  '+str(result[2])+'  '+str(result[3])+'  '+str(result[4])+'  '+str(result[5])+'  '+str(result[6])+'  '+str(result[7])+'  '+str(result[8])+'  '+str(result[9]))
        #       เลขแทร็ก             ขอนแก่น             มหาสารคาม            ร้อยเอ็ด               สุรินทร์              ชื่อคนส่ง              ชื่อคนรับ              ที่อยู่                 ราคา                น้ำหนัก
    if result[1] == 'LOE':
        c.execute('SELECT * FROM loei WHERE tracking = ?',search)
        conn.commit()
        result = c.fetchone()
        print(str(result[0])+'  '+str(result[1])+'  '+str(result[2])+'  '+str(result[3])+'  '+str(result[4])+'  '+str(result[5])+'  '+str(result[6])+'  '+str(result[7])+'  '+str(result[8]))
        #       เลขแทร็ก             ขอนแก่น             หนองบัวลำภู            เลย               ชื่อคนส่ง               ชื่อคนรับ               ที่อยู่              ราคา                 น้ำหนัก       

#final
while True:
    try:
        index()
        me = input('Enter your choice : ')
        if me == '1':        
            add()
        elif me == '2':
            update()
        elif me == '3':
            checking()
        elif me == 'x':
            try:
                x = input('Are you sure to close the prigram ? (y/n) : ')
                x = x.lower()
                if x == 'y':
                    break
                elif x == 'n':
                    print('\n')
            except:
                print('wrong! have problem in your anwer please try again ! \n')
    except:   
        print('wrong! have problem in your anwer please try again ! \n')                                          
conn.commit()
conn.close()