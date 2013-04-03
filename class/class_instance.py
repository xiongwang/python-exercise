class Fly:
    price = 123
    def __init__ (self):
        self.__direction = 'Train to Beijing'
        zIng = 'Waiting for train'

if __name__ == "__main__":
    print Fly.price
    fly = Fly()
    print fly._Fly__direction
    Fly.price = fly.price + 10
    print 'How\'s the waiting hall?'
    print 'Fee Rose! Damn' + str(fly.price)
    myfly = Fly()
    print 'Price I want: ' + str(myfly.price - 20)
