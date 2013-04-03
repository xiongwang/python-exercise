class Room:
    count = 0
    def __init__(self, name):
        self.name = name
        print 'initializing... name given was %s' %self.name
        Room.count += 1

    def __del__(self):
        print '%s Says goodbye' %self.name
        Room.count -= 1
        if Room.count == 0:
            print 'I\'m the last one here.'
        else:
            print 'There are %d People here.' %Room.count

    def sayHi(self):
        print 'My name is %s' %self.name

    def howMany(self):
        print 'There are still %d people here' %Room.count

if __name__ == "__main__":
    room = Room('WangXiong')
    room.sayHi()
    room.howMany()

    room1 = Room('Vivi')
    room1.sayHi()
    room1.howMany()

    room.__del__()
    #room1.__del__()

