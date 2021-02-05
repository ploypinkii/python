#งานสัปดาห์ที่ 2 นางสาวพลอยชมพู รุ่งพิสิฐไชย 633050135-6 

num1 =input('enter first number :')
num2 =input('enter second number :')
print(num1+"="+num2+" : ", num1 == num2)
print(num1+">"+num2+" : ", num1 > num2)
print(num1+"<"+num2+" : ", num1 < num2)

print(bool("hello"))
print(bool(""))


a = 60
b = 13 
c = 0

c = a & b
print(c)

c = a | b
print(c)

c = a ^ b
print(c)

c =~a
print(c)

c = a << 2
print(c)

c = a >> 2
print(c)

########################################################

#แบบฝึกหัดที่ 2.2 นางสาวพลอยชมพู รุ่งพิสิฐไชย 633050135-6
'''
day =int(input('Enter number of day :'))
print(day,"days : ",day*24,"hours")
print(day,"days : ",day*1440,"hours")
print(day,"days : ",day*86400,"hours")

friend = ['jan','cream','phu','bam','aom','pee','bas','kong','da','james']
friend[9]='may'
friend[3]='boat'
#print(friend[-4]) #เอาไว้บอกพิกัดว่าแสดงผลอันไหนบ้าง
#friend.remove('jan') #ลบข้อมูลออก
friend.append('dome')
friend.append('poondang')
friend.insert(1,'csa') #แทรกชื่อระหว่างชุดข้อมูล
friend.insert(7,'ped')
friend.remove('aom')
friend.pop() #ถ้าลบตัวสุดท้ายไม่ต้องใส
friend.pop(3)
del friend[7] #ตัวเลขเป็น [] เท่านั้น
friend.clear()
del friend
print(friend)
########################################################

#set
animal={'cat','dog','rat','pig','ant'}
animal.add('monkey')
animal.update(['python','capybara','spider','wombat','penguin','crocodile'])
#print(animal)

########################################################

#แบบฝึกหัด 2.3 นางสาวพลอยชมพู รุ่งพิสิฐไชย 633050135-6

shop = []
print('ร้านพลอยพิ้งค์สวัสดีค่ะ :))')
p1 = input('สินค้าชิ้นที่ 1 :')
shop.append(p1)
p2 = input('สินค้าชิ้นที่ 2 :')
shop.append(p2)
p3 = input('สิ้นค้าชิ้นที่ 3 :')
shop.append(p3)
p4 = input('สิ้นค้าชิ้นที่ 4 :')
shop.append(p4)
p5 = input('สิ้นค้าชิ้นที่ 3 :')
shop.append(p5)

print('รายการสินค้า มีดังนี้')
for i in range(5):
    print(i+1,shop[i]) #+1 มีความหมายว่าเริ่มตั้งแต่เลขอะไร

########################################################

#แบบฝึกหัด 2.4 นางสาวพลอยชมพู รุ่งพิสิฐไชย 633050135-6 
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
    '''