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
'''

#แบบฝึกหัดที่ 4.1 นางสาวพลอยชมพู รุ่งพิสิฐไชย 633050135-6
#ยังไม่เสร็จคับ
'''
shop = []
numorder = []
i = 1
def preview():
    print('1. ชานมใต้หวัน : 20 บาท\n2. ชานมโกโก้ : 20 บาท\n3. ชาเขียว : 25 บาท\n4. ชานมเมล่อน : 25 บาท\nทุกออเดอร์ใส่ไข่มุกฟรี')

def menu():
    print('A : แสดงรายการสินค้า\nB : เลือกสินค้า\nC : แสดงสินค้าที่เลือก\nX : ออกจากโปรแกรม')

def order():
    print('พวยพิ้งชานมไข่มุก')
    menu()
    a=input('เลือกรายการ :')
    a = a.lower()
order()

while True:
    if a == 'a':
        preview()
        break
    elif a == 'b':
        
    #elif a == 'c':
       print('รายการสินค้าที่คุณเลือก มีดังนี้')


def Introduce(arg1,arg2 = 'com', arg3 = 'ed',arg4 = 'Kku') :
    print('Hello,I am ' + arg1 +','+arg2+','+arg3+','+arg4)
Introduce('ploy')
Introduce(arg1='python')
Introduce(arg1='plython',arg3='sci')
Introduce('python',arg4='cmu')
'''
#แบบฝึกหัดที่ 4.2 นางสาวพลอยชมพู รุ่งพิสิฐไชย 633050135-6
'''
vocab = ['']
typev = ['']
means = ['']
def menu():
    print('พจนานุกรม\n1) เพิ่มคำศัพท์\n2) แสดงคำศัพท์\n3) ลบคำศัพท์\n4) ออกจากโปรแกรม')

def add():
    addvocab=input('เพิ่มคำศัพท์ :')
    vocab.append(addvocab)
    tv=input('ชนิดคำ (n,adv,adj,v) :')
    typev.append(tv)
    mean=input('ความหมาย :')
    means.append(mean)
    print('เพิ่มคำศัพท์เรียบร้อยแล้ว')

def preview():
    print('-'*20)
    print(' '*2 +"คำศัพท์ของคุณมีดังนี้")
    print('-'*20)
    print('{0:-<10}{1:-<10}{2:<10}'.format('คำศัพท์','ประเภท','ความหมาย'))
    for i in range(0,len(vocab)) :
        print('{0:-<10}{1:-<10}{2:-<10}'.format(vocab[i],typev[i],means[i]))

def cut():
    d=input('พิมพ์คำศัพท์ที่ต้องการลบ :')
    q=input('แน่ใจใช่ไหมว่ต้องการลบ ? (y/n) :')
    if q == 'y' :
        vocab.remove(d)
        print('ลบคำศัพท์เรียบร้อยแล้ว')
    else :
        print('')

while(True):
    menu()
    me=int(input('เลือกรายการที่ต้องการ :'))
    if me == 1 :
        add()
    elif me == 2 :
        preview()
    elif me == 3 :
        cut()
    else:
        break
'''

#แบบฝึกหัดที่ 4.2 นางสาวพลอยชมพู รุ่งพิสิฐไชย 633050135-6
word = ['Thailand','Chinese','Korea']
typev = ['n','adj','v']
mean = ['ไทย','จีน','เกาหลี']

final =dict(zip(word,typev))
print(final)

#dict = {'word':',''type':'','mean':''}
#dict = {'word':[pink,adj,สีชมพู]}
'''
def add():
    w =input('เพิ่มคำศัพท์ :')
    dict['word'] = w
    t =input('ชนิดของคำ(n,v,adj,adv) :')
    dict['type'] = t
    m =input('ความหมาย :')
    dict['mean'] = m

def rem():
    d =input('พิมพ์คำศัพท์ที่ต้องการลบ :')
    q =input('คุณต้องการลบคำศัพท์ใช่หรือไม่ (y/n) :')
    if q == 'y':
        del dict['word'] =d
    else :
        print('')
