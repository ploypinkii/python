import sqlite3
conn = sqlite3.connect(r"D:\ED\term2\ED251007\ploychomphu_python\homework6.py")
def in_put():
     while(True):
        name_s = input("กรุณากรอกข้อมูล\nชื่อ-สกุลนักนักศึกษา:\t")
        email_s = input("E-mail:\t")
        sex_s = input("เพศ:\t")
        age_s = input("อายุ:\t")
        year_s = input("ชั้นปี\t")
        c = conn.cursor()
        data = ("{0: <40}".format(name_s),"{0: <40}".format(email_s),"{0: <5}".format(sex_s),"{0: <5}".format(age_s),year_s)
        c.execute('INSERT INTO pink (name,email,sex,age,year) VALUES (?,?,?,?,?)',data)
        conn.commit()
        c.close()
        yn = input("ทำรายการเสร็จสิ้น\nคุณต้องการเพิ่มข้อมูลอีกหรือไม่(y/n):")
        if yn == 'n':
            break
def out_put():
    print("{0: <10}{1: <40}{2: <40}{3: <5}{4: <5}{5}".format("ลำดับ","ชื่อ-นามสกุล","อีเมล","เพศ","อายุ","ชั้นปี")+"\n",100*"-")
    c = conn.cursor()
    c.execute('''SELECT * FROM pink ''')
    result = c.fetchall()
    for i in result:
        print(i)
    c.close()
def edi():
    num = int(input("กรุณาพิมลำดับนักษาที่คุนต้องการแก้:\t"))
    name_s = input("กรุณากรอกข้อมูล\nชื่อ-สกุลนักนักศึกษา:\t")
    email_s = input("E-mail:\t")
    sex_s = input("เพศ:\t")
    age_s = input("อายุ:\t")
    year_s = input("ชั้นปี:\t")
    c = conn.cursor()
    data = ("{0: <40}".format(name_s),"{0: <40}".format(email_s),"{0: <5}".format(sex_s),"{0: <5}".format(age_s),year_s,num)
    c.execute('''UPDATE pom SET name =?,email =?,sex =?,age =?,year =? WHERE id = ? ''',data)
    conn.commit()
    c.close()
def dele():
    yn = input("คุณต้องการลบข้อมูลใช่หรือไม่(y/n):")
    if yn == 'y':
        num = input("กรุณษพิมลำดับนักศึกษาที่ต้องการลบ:")
        c = conn.cursor()
        c.execute('DELETE FROM pom WHERE id = ?',num)
        conn.commit()
        c.close()
        print("ทำการลบเรียบร้อย")
while(True):
    print("="*30,"\n--ระบบทะเบียนนักศึกษา--\n","="*30+"\nเพิ่มนักศึกษากด [a]\nแสดงข้อมูลนักศึกษา [s]\nแก้ไขข้อมูลนักศึกษา [e]\nลบข้อมูลนักศึกษา [d]\nออกจากโปรแกรม [x]")
    x = input("\nกรุณานาเลือกทำรายการ :\t")
    if x == 'a':
        in_put()
    elif x == 's':
        out_put()
    elif x == 'e':
        edi()
    elif x == 'd':
        dele()
    else:
        yn = input("คุณต้องการออกจากระบบใช่หรือไม่ๅ(y/n):")
        if yn == 'y':
            break