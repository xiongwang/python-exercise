class Person(object):
    def __init__(self, name):
        self.name = name
        print 'initialized name = %s' %self.name

class Ordinary(Person):
    def __init__(self, name):
        super(Ordinary.self).__init__()
        print 'Ordinary Man'

if __name__ == "__main__":
    print issubclass(Ordinary, Person)
    #check if an instance of class
    person = Person('wangxiong')
    print isinstance(person, Person)

