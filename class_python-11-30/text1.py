class Student:
    def __init__(self, SchoolName, SchoolAddress, Chairman, StuName, StuID, Email, Credit, GPA):
        # 建構子，用來初始化學生物件的屬性
        self.SchoolName = SchoolName
        self.SchoolAddress = SchoolAddress
        self.Chairman = Chairman
        self.StuName = StuName
        self.StuID = StuID
        self.Email = Email
        self.Credit = Credit
        self.GPA = GPA

    def getSchoolName(self):
        # 取得學校名稱的方法
        print(self.SchoolName)

    def setSchoolName(self, SchoolName):
        # 設定學校名稱的方法
        self.SchoolName = SchoolName
        print(SchoolName)

    def getSchoolAddress(self):
        # 取得學校地址的方法
        print(self.SchoolAddress)

    def setSchoolAddress(self, SchoolAddress):
        # 設定學校地址的方法
        self.SchoolAddress = SchoolAddress
        print(SchoolAddress)
    
    def getChairman(self):
        # 取得系主任姓名的方法
        print(self.Chairman)

    def setChairman(self, Chairman):
        # 設定系主任姓名的方法
        self.Chairman = Chairman
        print(Chairman)
    
    def getStuName(self):
        # 取得學生姓名的方法
        print(self.StuName)

    def setStuName(self, StuName):
        # 設定學生姓名的方法
        self.StuName = StuName
        print(StuName)

    def getStuID(self):
        # 取得學生學號的方法
        print(self.StuID)

    def setStuID(self, StuID):
        # 設定學生學號的方法
        self.StuID = StuID
        print(StuID)
    
    def getEmail(self):
        # 取得學生Email的方法
        print(self.Email)

    def setEmail(self, Email):
        # 設定學生Email的方法
        self.Email = Email
        print(Email)
    
    def getCredit(self):
        # 取得學分數的方法
        print(self.Credit)

    def setCredit(self, Credit):
        # 設定學分數的方法
        self.Credit = Credit
        print(Credit)
    
    def getGPA(self):
        # 取得GPA的方法
        print(self.GPA)

    def setGPA(self, GPA):
        # 設定GPA的方法
        self.GPA= GPA
        print(GPA)

# 建立一個學生物件
student = Student("ABC 大學", "123 主街", "熊主任", "阿熊", "A7654321", "nlnlqwq@email.com", 55, 3)

# 使用 getter 和 setter 方法
student.getSchoolName()
student.setSchoolName("XYZ 大學")

student.getSchoolAddress()
student.setSchoolAddress("456 大街")

student.getChairman()
student.setChairman("熊主任")

student.getStuName()
student.setStuName("阿瘸")

student.getStuID()
student.setStuID("B1234567")

student.getEmail()
student.setEmail("nlnlqwq@email.com")

student.getCredit()
student.setCredit(75)

student.getGPA()
student.setGPA(3.8)
