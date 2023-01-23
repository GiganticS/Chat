#please firstly run the server.py#
import socket

socket_server = socket.socket()

username = input("Type your name: ")
#connecting to my server#
socket_server.connect(("127.0.0.1", 50))
socket_server.send(username.encode())
socket_name = socket_server.recv(1024)
server_name = socket_name.decode()
print("Your are in!")
#making infinite loop that will send/wait messages
while True:
    message = (socket_server.recv(1024)).decode()
    print(server_name + ': ' + message)
    message = input("You: ")
    socket_server.send(message.encode())
