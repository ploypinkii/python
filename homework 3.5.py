#งานชิ้นที่ 3.5 นางสาวพลอยชมพู รุ่งพิสิฐไชย 633050135-6
n =int(input('please enter student :'))
num = [0,0,0,0,0,0]
score = ['90-100','80-89','70-79','60-69','50-59','0-49']
for i in range(0,n):
    st =int(input('Enter student score :'))
    if st <= 100 and st >= 90 :
        num[0] +=1 
    elif st <= 89 and st >=80 :
        num[1] +=1
    elif st <= 79 and st >=70 :
        num[2] +=1
    elif st <=69 and st >=60 :
        num[3] +=1
    elif st <=59 and st >=50 :
        num[4] +=1
    else :
        num[5] +=1
for i in range(0,6):
    print(score[i]+':'+num[i]*'*')
    