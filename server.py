#importing the main library#
import socket
#making socket variable and then running the server#
new_socket = socket.socket()
new_socket.bind(("127.0.0.1", 50))
new_socket.listen()

print("Server is running")

username = input("Type in your name: ")

conn, add = new_socket.accept()

client = (conn.recv(1024)).decode()
print("You are in")
conn.send(username.encode())
#making infinite loop so we can use until we will be bored#
while True:
    message = input("Type in: ")
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(client + ':' + message)
