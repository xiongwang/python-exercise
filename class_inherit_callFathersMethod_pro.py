class Person(object):
    def __init__(self, name):
        self.name = name
        print 'I\'m %s' %self.name

class Star(Person):
    def __init__(self, name):
        super(Star, self).__init__(name)
        print 'Star'

if __name__ == "__main__":
    Star('fuck')
