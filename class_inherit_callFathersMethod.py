class Father:
    def __init__(self):
        print 'Father\'s Method'
        print 'To be called'

class Son(Father):
    def __init__(self):
        print 'Son\'s Method'
        Father.__init__(self)

if __name__ == "__main__":
    b = Son()

