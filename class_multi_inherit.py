class MyFather:
    def __init__(self):
        self.eyes = 'Black'
        print self.eyes

class MyMother:
    def __init__(self):
        self.forehead = 'Headache'
        print self.forehead

class MyGrandpa:
    def __init__(self):
        self.nose = 'High'
        print self.nose


#this is the inherited class
class Myself(MyFather, MyMother, MyGrandpa):
    def __init__(self, face):
        print 'I got something from my father: '
        MyFather.__init__(self)

        print 'I also got something from my mother: '
        MyMother.__init__(self)

        print 'I also got something from my grandpa: '
        MyGrandpa.__init__(self)
        
        self.face = face
        print 'But My face is unique! it\'s %s' %self.face

if __name__ == "__main__":
    myself = Myself('Round')
