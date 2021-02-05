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