import os
def ListDir(path, fun, par):
    for filespath in par:
        #print 'now listing contents in /home'
        #difference between os.walk & os.path.walk
        #os.walk(): can't travel over sub folders
        #os.path.walk(): powerful enough to travel over sub folders
        print os.path.join(fun, filespath).strip("./")
        #BTW, we use os.path.join() to combine filename and path

if __name__ == "__main__":
    os.path.walk("./", ListDir, ())
