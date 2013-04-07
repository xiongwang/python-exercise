import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345

#BE CAREFUL
#bing() only takes one arg - host/port pair
s.bind(("127.0.0.1", port))
s.listen(5)

while True:
    c, addr = s.accept()
    print 'Request from: ', addr
    c.send('Connect Established!')
    c.close()
