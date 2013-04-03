class MyLimter(object):
    __slot__ = 'myname', 'myage', 'myhobby'

if __name__ == "__main__":
    x = MyLimter()
    x.myname = 'wangxiong'
    #this statment will raise error
    #you can't add new attributes freely any more
    #x.name = 'wangxiong'

