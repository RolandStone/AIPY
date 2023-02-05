import socket

# get the IP address and port from the user
ip = input("Enter the IP address of the server: ")
port = int(input("Enter the port number: "))

# create a client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip, port))

# get the username from the user
username = input("Enter your username: ")

# send the username to the server
client_socket.sendall(username.encode())

while True:
    # receive messages from the server
    message = client_socket.recv(1024).decode()
    if not message:
        continue
    
    print(message)
    
    # get a message from the user
    message = input()
    
    # send the message to the server
    client_socket.sendall(message.encode())
