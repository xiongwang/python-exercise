class MyNamespace:
    count = 1
    def myinit (self):
        MyNamespace.count += 1

if __name__ == "__main__":
    mynamespace = MyNamespace()
    mynamespace.myinit()
    print mynamespace.count
