socket programming  - > 
 
sockets 

internet has a lot of nodes 

nodes can be servers or they can be clints

p2p peer to peer network  clients talk to eahc other




consepts to learn -> 
port consept  -- port numbers 

when you have a server it will have an ip address to communicate we need an ip address this ip adress can also have a name eg google.com 

if you have a machine and this machine will provide you with many services every service will have a different port no . eg if http service is running it will have a port no port no sholud be different for different services
two thing can not runs on a single port no 


tcp and udp 

tcp - > transmission control protocol (connection oriented) 
we need to have a connection in order to communicate first

udp - > user datagram protocol connectionless and based on the address it will reach the destination

not sure that the packet will reach there


we will work on tcp 

we need ttwo files 

seerver and client  -> 
 
---------------------------------------------------------------------------

importing libraries  -> 


in server.py-->>>>>

import socket 

s = socketname.socket()  

//socket is a function 2 paramiters type of network ipv4/v6 and type of network tcp or udp ======== by default it will be ipv4 and tcp


print socket created

//then we have to bind a socket with a port number as this is a server socket it will accept the connections for that it will need a port no that the client can reach .it will accept the connection
it will have an ip adress now we need a port no .

// how will we do that  ? 

function called bind 

s.bind(("localhost",9999))  //bind takes only 1 argument therefore we have to pass 2 args as one 

 // adress we will be using will be loCAL host and and a free port no  the range of the port numbers will start from 0-65535


// now the next step is to listen to the client but  at one point how many clinet we will be listning to  ?

1-2-3-4---10??

s.listen(3)

print waiting for connection

 ///if 4 are triying to connect it will be refused 


while true :
     c, addr = s.accept()
     
     name = c.recv(1024).decode()


     print client connected ,addr , name

this is responcible to get the connection it will return 2 things 1- client socket and it will also give you the address of the client 
     
thenn we will send somethings to client by the function send 

     c.send('message from server - > hello ')

 then for closig the connction ->

     c.close()

server is done 

the message from server should be send into a byte fromat and not string therefore 

c.send(bytes("message from server",'utf-8')

and we also need to specify the frommat eg utf 8 frormat


run the server first 
-------------------------------------------------------------------


in client.py

import socket 

c= socketname.socket()

 again 2 parameters ipv4 and tcp both default

c.connect(('localhost',9999))

where will the client connect ?? which ip and wchich port no to connect

then the message from the server should be printed 

as  

name=imput('enter your name  - ')
c.send(bytes(name,'utf-8')

this will send the data to server 

print(c.recv(1024).decode)

by decode it will not specify the format
also we have to specify the size of the msg 



