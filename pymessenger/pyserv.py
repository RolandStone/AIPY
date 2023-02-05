import socket

port = int(input("Enter the port number: "))

# create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', port))
server_socket.listen()

# keep a list of all connected clients
clients = []
usernames = {}

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            client.sendall(message)

while True:
    # accept incoming connections
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    # receive the username from the client
    username = client_socket.recv(1024).decode()
    usernames[client_socket] = username
    print(f"Username for {client_address} is {username}")

    # add the new client to the list of clients
    clients.append(client_socket)

    # broadcast a message to all clients to inform them of the new connection
    broadcast(f"{username} has joined the chat".encode(), client_socket)

    while True:
        try:
            # receive data from the client
            data = client_socket.recv(1024).decode()
            if not data:
                continue
            
            print(f"{username} sent message: {data}")
            
            # send the received data to all connected clients
            broadcast(f"{username}: {data}".encode(), client_socket)
        except ConnectionResetError:
            # the client disconnected, so remove it from the list of clients
            clients.remove(client_socket)

            # broadcast a message to inform the other clients of the disconnection
            broadcast(f"{username} has left the chat".encode(), client_socket)
            break
