import socket

c = socket.socket()
c.connect(('localhost', 9999))

while True:
    start = int(input("Enter 0 to start: "))
    if start != 0:
        break

    print("\n\nConnected to server. \nHelpline active .. ! \nYou can now ask a quiry.\n")
    print("=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    while True:
        msg = input("\nEnter your message - ")
        c.send(bytes(msg, 'utf-8'))
        
        print("\nPlease wait for us to reply ... ")

        response = c.recv(1024).decode()
        print("\nResponse from the helpline - \n\n",response)
        print("\n=======================================================")
        continue_chat = int(input("\nEnter 0 to continue chatting: "))
        print("--------------------------------------------------------")
        if continue_chat != 0:
            break

c.close()
print("Connection closed.")