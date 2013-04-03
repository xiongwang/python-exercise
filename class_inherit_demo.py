class schoolMember:
    def __init__(self, name, age, addr, hobby):
        self.name = name
        self.age = age
        self.addr = addr
        self.hobby = hobby
        print 'initialized name %s' %self.name

    def tell(self):
        print 'Name: %s, Age:%s, Add:%s, Hobby:%s' %(self.name, self. age, self.addr, self.hobby)

class Teacher(schoolMember):
    def __init__(self, name, age, addr, hobby, salary):
        schoolMember.__init__(self, name, age, addr, hobby)
        self.salary = salary
        print 'Inherit schoolMember\'s Name: %s' %self.name
    
    def tell(self):
        schoolMember.tell(self)
        print 'My Salary is %s' %self.salary

class Student(schoolMember):
    def __init__(self, name, age, addr, hobby, marks):
        schoolMember.__init__(self, name, age, addr, hobby)
        self.marks = marks
        print 'Student Inherited from schoolMember %s' %self.name

    def tell(self):
        schoolMember.tell(self)
        print 'My Mark is %d' %self.marks

if __name__ == "__main__":
    t = Teacher('abc', 40, 'WTF', 'Tour', 3000)
    s = Student('cde', 22, 'Damn', 'Tour', 100)
    members = [t, s]
    for member in members:
        member.tell()

