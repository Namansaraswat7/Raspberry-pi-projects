import socket               # Import socket module

s = socket.socket()         # Create a socket object
port = 12345                # Reserve a port for your service.
s.bind(('', port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print ('Got connection from', addr)
      c.send(b'chutiya')
    
