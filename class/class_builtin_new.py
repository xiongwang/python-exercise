class MyNew(object):
    def __init__(self):
        print '__init__'
    def __new__(self):
        print '__new__'

if __name__ == '__main__':
    mynew = MyNew()
    mynew
