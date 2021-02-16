#ใบงานที่ 5.1 นางสาวพลอยชมพู รุ่งพิสิฐไชย 633050135-6

def add():
    global name,grade,department,faculty,province
    print('*'*20+'แนะนำตัว'+'*'*20)
    add = input('ชื่อ-สกุล : ชั้นปีการศึกษา : สาขาวิชา : คณะ : จังหวัด (คั่นด้วยเครื่องหมาย / )       ')
    addnew= add.split('/')
    name = addnew[0]
    grade = addnew[1]
    department = addnew[2]
    faculty = addnew[3]
    province = addnew[4]
class nisit :        
    def __init__(self,name,grade,department,faculty,province):
        self.name = name
        self.grade = grade
        self.department = department
        self.faculty = faculty
        self.province = province
    def showname(self):
        print('สวัสดีค่ะ ดิฉันชื่อ  '+self.name+'   นักศึกษาชั้นปีที่ '+self.grade+' สาขา'+self.department+' คณะ'+self.faculty+' มาจากจังหวัด '+self.province)
add()
x = nisit(name,grade,department,faculty,province)
x.showname()