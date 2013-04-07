from SocketServer import TCPServer, StreamRequestHandler
class Handler(StreamRequestHandler):
    def handle(self): #Override Handler
        addr = self.request.getpeername() #Get Peer Address
        print 'Got request from: ', addr
        self.wfile.write('Connection Established...') #Send Data
server = TCPServer((' ',12345), Handler) #Get TCP Server
server.serve_forever() #Start Listening and Handle Connection


