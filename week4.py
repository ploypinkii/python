#งานสัปดาห์ที่ 4 นางสาวพลอยชมพู รุ่งพิสิฐไชย 633050135-6
'''
import os
choice = 0
filename = ''

def menu():
    global choice
    print('Menu\n 1.open file explorer\n 2.Open Notepad\n 3.Exit')
    choice = input('Select Menu :')

def opennotepad():
    filename = 'C:\\Windows\\notepad.exe'
    print('Memorandum writing %s' %filename)
    os.system(filename)

def openfileexplorer():
    filename = 'C:\\Windows\\explorer.exe'
    print('Calculator Number %s' %filename)
    os.system(filename)

while True:
    menu()
    if choice == '1':
        openfileexplorer()
    elif choice == '2':
        opennotepad()
    else:
        break

########################################################

#งานที่ 4.1 นางสาวพลอยชมพู รุ่งพิสิฐไชย 633050135-6 
order = {'order':[0,0,0,0,0],'count':[0,0,0,0,0],'price':[20,20,25,25,25]}

def menu():
    print(' ')
    print('PP BUBBLE TEA\n1.แสดงรายการสินค้า\n2.เลือกสินค้า\n3.แสดงรายการที่เลือก\n4.ปิดโปรแกรม')

def preview():
    print('MENU\n1.ชานมใต้หวัน        20  บาท\n2.ชานมโกโก้         20  บาท\n3.ชาเขียว           25  บาท\n4.ชานมสตอเบอร์รี่     25  บาท\n5.ชามะลิ            25  บาท\n***ทุกรายการใส่ไข่มุกฟรี***')

def pick():
    i = 0
    while (True):
        p =input('เลือกเมนูที่ต้องการ หรือกด 6 เพื่อออกจากหน้านี้ :')
        if p == '1':
            order['order'][0] = 'ชานมใต้หวัน' 
        elif p == '2':
            order['order'][1] = 'ชานมโกโก้'
        elif p == '3':
            order['order'][2] = 'ชาเขียว'
        elif p == '4':
            order['order'][3] = 'ชานมสตอเบอร์รี่'
        elif p == '5':
            order['order'][4] = 'ชามะลิ'
        else:
            break
        c =int(input('จำนวน :'))
        order['count'][i] += c
        i+=1

def preorder():
    print('-'*50)
    print('-'*10 +"รายการสั่งซื้อของคุณมีดังนี้"+'-'*10)
    print('-'*50)
    print('{0:-<15}{1:-<15}{2:-<10}'.format('รายการ','จำนวน','ราคา'))
    for i in range(0,5):
        print('{0:-<15}{1:-<15}{2:-<15}'.format(order['order'][i],order['count'][i],order['price'][i]))


while True:
    menu()
    m = int(input('เลือกทำรายกาารที่ :'))
    if m == 1:
        preview()
    elif m == 2:
        preview()
        pick()
    elif m == 3:
        preorder()
    else:
        q =input('คุณแน่ใจใช่ไหมว่าต้องการออกจากโปรแกรม (y/n) :')
        if q =='y':
            break
        else:
            print(' ')

############################################################

#ใบงานที่ 4.2 นางสาวพลอยชมพู รุ่งพิสิฐไชย 633050135-6 
word = {}
def menu():
    print('พจนานุกรม\n1) เพิ่มคำศัพท์\n2) แสดงคำศัพท์\n3) ลบคำศัพท์\n4) ออกจากโปรแกรม')
def add():
    w =input('เพิ่มคำศัพท์ : ')
    t =input('ชนิดคำศัพท์(n,v,adj,adv) :')
    m =input('ความหมาย :')
    word.update({w:{m,t}})
def view():
    print('-'*50)
    print(' '*18 +"คำศัพท์ของคุณมีดังนี้"+' '*18)
    print('-'*50)
    print('{0:-<15}{1:-<15}{2:-<10}'.format('คำศัพท์','ประเภท','ความหมาย'))
    for k,v in word.items():
        print(k+'           ',v)
def remove():
    r =input('พิมพ์คำศัพท์ที่ต้องการลบ :')
    q =input('คุณแน่ใจใช่ไหมว่าต้องการลบ (y/n) :')
    if q == 'y':
        word.pop(r)
    else:
        print(' ')

while True:
    menu()
    me =int(input('เลือกรายการที่ต้องการ :'))
    if me == 1:
        add()
    elif me == 2:
        view()
    elif me == 3:
        remove()
    else:
        q =input('คุณแน่ใจใช่ไหมว่าต้องการออกจากโปรแกรม ? (y/n) :')
        if q == 'y':
            break
        else:
            print('')

###########################################################################3

#ใบงานที่ 4.3 นางสาวพลอยชมพู รุ่งพิสิฐไชย 633050135-6
import datetime
name,pts,time,hit=[],[],[],[]
num =int(input('Enter number of Competitor     : '))
for i in range(num):
    print(i+1,'of Comprtitor')
    regname =input('Name of Competitor             : ')
    regpts =int(input('Enter your PTS                 : '))
    regtime =float(input('Enter your time                : '))
    name.insert(i,regname),pts.insert(i,regpts),time.insert(i,regtime),hit.insert(i,regpts/regtime)
for i in range(num):
    j = i
    for j in range(num):
        if pts[i] > pts[j]:
            a,b,c,d = hit[i],name[i],pts[i],time[i]
            hit[i],name[i],pts[i],time[i]=hit[j],name[j],pts[j],time[j]
            hit[j],name[j],pts[j],time[j]=a,b,c,d
date = datetime.datetime.now()
datenew = date.strftime('%G-%m-%d %H:%M:%S')
print('\nShotgun',date.strftime('%A'),'Training',date.strftime('%Y'))
print(datenew)
print('-'*110+'\n{0:-<15}{1:-<15}{2:-<15}{3:-<20}{4:-<15}{5:-<15}{6:-<15}'.format('No.','PTS','TIME','COMPETITOR','HIT FACTOR','STATE POINTS','STATE PERCENT\n'+'-'*110))
for i in range(num):
    print('{0: <15}{1: <15}{2: <15}{3: <20}{4: <15}{5: <15}{6: <1}'.format(i+1,pts[i],time[i],name[i],'%.4f'%hit[i],'%.4f'%float(hit[i]/hit[0]*50),'%.4f'%float((hit[i]/hit[0]*50)/(hit[0]/hit[0]*50)*100)))
'''