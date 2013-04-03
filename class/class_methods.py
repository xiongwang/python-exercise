class MyS1(object):
    def myfoo(self, myself):
        #method of instances
        print 'Do Instance\'s Method foo (%s, %s)' %(self, myself)

    @classmethod
    def class_foo(cls, mycls):
        #method of classes
        print 'Do Class\'s Method class_foo(%s, %s)' %(cls, mycls)

if __name__ == "__main__":
    mys1 = MyS1()
    mys1.myfoo('what')
    mys1.class_foo('damn')
    MyS1.class_foo('fuck')

