def among():
    print 'this is among()'

def ending():
    print 'this is ending()'

class Person:
    def began(self):
        print 'began() inside Person Class'
    

if __name__ == '__main__':
    print 'First Way to get much money as you want:'
    person = Person()
    person.began()
    print 'Second Way to get money:'
    person.began = among
    person.began()
    print 'Third Way to get money:'
    person.began = ending
    person.began()

