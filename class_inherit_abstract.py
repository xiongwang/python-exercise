def abstract():
    raise NotImplementedError("abstract")

class Person:
    def __init__(self):
        if self.__class__ is Person:
            abstract()

class Star(Person):
    def __init__(self):
        Person.__init__(self)
        print 'I\'m star!'

if __name__ == "__main__":
    #It's OK to implement a normal class
    star = Star()
    #It will be error to implement a abstract class
    person = Person()


