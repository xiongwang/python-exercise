class Fruit:
    def __init__(self, *args):
        for arg in args:
            arg(self)
    def config(self, *args):
        for arg in args:
            arg(self)

#to get the apple is ok or not
def has_harvest(self):
    self.harvest = True
def has_not_harvest(self):
    self.harvest = False

#to get the color of apple
def setColor(color):
    def method(self):
        self.color = color
    return method

#to know if apple can be eaten
def can_eat(self):
    self.eat = True
def can_not_eat(self):
    self.eat = False


if __name__ == "__main__":
    apple = Fruit(has_not_harvest, setColor('green'))
    print '----%s, %s-----' %(apple.harvest, apple.color)

    apple.config(has_harvest, setColor('red'), can_not_eat)
    print '----%s, %s, %s-----' %(apple.harvest, apple.color, apple.eat)

    apple.config(has_harvest, setColor('red'), can_eat)
    print '----%s, %s, %s-----' %(apple.harvest, apple.color, apple.eat)
