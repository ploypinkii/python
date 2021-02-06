#งานชิ้นที่ 3.3 นางสาวพลอยชมพู รุ่งพิสิฐไชย 633050135-6

print('ป้อนชื่ออาหารสุดโปรดของคุณ หรือ exit เพื่อแสดงผลและออกจากโปรแกรม')
food=[]
i = 1
a = 0
s = 0
c = 1
while (True):
    if a == 'exit':
        food.remove('exit')
        break
    else :
        a=input('อาหารโปรดอันดับที่ '+str(i)+ ' คือ    ')
        food.append(a)
        i+=1
    
print('\nอาหารโปรดของคุณมีดังนี้\n')
while (s<=i):
        print(str(c)+'. '+food[s])
        s+=1
        c+=1