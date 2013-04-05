# -*- coding: UTF-8 -*-
import os

print '-------test program for read/write ---------'
con = True

while con:
    choice = raw_input("[1].Write [2].Read [3].Erase [4].Quit\n")
    if (choice == "1"):
        file_thing = open('io_file', 'w')
        content = raw_input('please input:\n')
        file_thing.write(content)
        file_thing.close()
        print "\n"
    elif (choice == "2"):
        print 'the content was:\n'
        file_thing = open('io_file', 'a+')
        listcontent = file_thing.readlines()
        for content in listcontent:
            print content
        file_thing.close()
        print "\n"
    elif (choice == "3"):
        sure = raw_input("Will Erase Everything, Press Y for Sure: ")
        if (sure == "Y"):
            print 'Deleting\n'
            if os.path.exists("io_file"):
                os.remove("io_file")
                print "Deleted Successfully!\n"
            else:
                print "Oops, File not found\n"
    elif (choice == "4"):
        print 'Exiting...'
        choice = False
        os._exit(1)

    else:
        print 'Error Input!'
        choice = False
        #exit(3)
        os._exit(1)
