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