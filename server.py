import socket

s = socket.socket()
s.bind(('localhost', 9999))
s.listen(1)
print("Server started. Listening on port 9999...")

while True:
    c, addr = s.accept()
    print("Client connected from - ", addr)

    while True:
        clientmsg = c.recv(1024).decode()
        if not clientmsg:
            break
        
        print("\n=============================================")
        print('\nCustomer quiry -\n\n',clientmsg)
        msgToClient = input("\nYour reply to quiry - ")
        c.send(bytes(msgToClient, 'utf-8'))

    c.close()
    print("Connection closed by the client.")