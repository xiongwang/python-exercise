class Methods:
    @staticmethod
    def mymethod():
        print 'this is static method defined'
    def __mymethod():
        print 'this is private method'
    def getMymethod():
        print 'this is test method for convert'

    conversion = staticmethod(getMymethod)
    conPrivate = staticmethod(__mymethod)

if __name__ == "__main__":
    methods = Methods()
    
    methods.mymethod()
    Methods.mymethod()
    Methods.conversion()
    methods.conversion()
    Methods.conPrivate()
    methods.conPrivate()

