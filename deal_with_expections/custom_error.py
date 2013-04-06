class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

if __name__ == "__main__":
    try:
        raise MyError(2*3)
    except MyError, e:
        print 'Error Occurred, Value:', e.value

