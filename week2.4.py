#ใบงานที่ 2.4 นางสาวพลอยชมพู รุ่งพิสิฐไชย 633050135-6
four = {
    'ลาดกระบัง-บางบ่อ' : '30 บาท',
    'ลาดกระบัง-บางปะกง' : '45 บาท',
    'ลาดกระบัง-พนัสนิคม' : '55 บาท',
    'ลาดกระบัง-บ้านบึง' : '60 บาท',
    'ลาดกระบัง-บางพระ' : '80 บาท'
}

six = {
    'ลาดกระบัง-บางบ่อ' : '45 บาท',
    'ลาดกระบัง-บางปะกง' : '45 บาท',
    'ลาดกระบัง-พนัสนิคม' : '75 บาท',
    'ลาดกระบัง-บ้านบึง' : '90 บาท',
    'ลาดกระบัง-บางพระ' : '100 บาท'
}

moresix = {
    'ลาดกระบัง-บางบ่อ' : '60 บาท',
    'ลาดกระบัง-บางปะกง' : '70 บาท',
    'ลาดกระบัง-พนัสนิคม' : '110 บาท',
    'ลาดกระบัง-บ้านบึง' : '130 บาท',
    'ลาดกระบัง-บางพระ' : '140 บาท'
}
print('โปรแกรมคำนวณค่าผ่านทางมอเตอร์เวย์')
print('รถยนต์ 4 ล้อ กด 1\nรถยนต์ 6 ล้อ กด 2\nรถยนต์มากกว่า 6 ล้อ กด 3\n')

a=int(input('เลือกประเภทพาหนะ :'))
if a==1:
    print('ค่าบริการรถยนต์ 4 ล้อ')
    print(*four.items(), sep='\n')
if a==2:
    print('ค่าบริการรถยนต์ 6 ล้อ')
    print(*six.items(), sep='\n')
if a==3:
    print('ค่าบริการรถยนต์มากกว่า 6 ล้อ')
    print(*moresix.items(), sep='\n')