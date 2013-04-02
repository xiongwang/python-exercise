class BuiltAttribute:
    def __init__(self):
        self.built = 'built-in attributes inside "__init__" '

class AttendBuilt(BuiltAttribute):
    def accept(self):
        self.acceptAttend = 'attribute inside accept()'

if __name__ == "__main__":
    buildattribute = BuiltAttribute()
    attendbuilt = AttendBuilt()
    print attendbuilt.built
    #print AttendBuilt.__bases__
    print attendbuilt.__dict__
    print attendbuilt.__module__
    print attendbuilt.__doc__
    print AttendBuilt.__name__
    print AttendBuilt.__bases__
