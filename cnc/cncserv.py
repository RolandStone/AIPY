import socket

# Ask the user for the IP address to bind the server socket to
bind_ip = input("Enter the IP address to bind the server socket to (e.g. 0.0.0.0): ")

# Ask the user for the port to bind the server socket to
bind_port = int(input("Enter the port to bind the server socket to (e.g. 8080): "))

# Set up the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((bind_ip, bind_port))
server_socket.listen(5)

# Store valid username and password combinations
valid_credentials = {
    "user1": "password1",
    "user2": "password2"
}

def handle_client(client_socket, client_address):
    print(f"Accepted connection from {client_address}")

    # Receive the username and password from the client
    username = client_socket.recv(1024).decode().strip()
    password = client_socket.recv(1024).decode().strip()

    # Check if the provided username and password are valid
    if username in valid_credentials and valid_credentials[username] == password:
        client_socket.send(b"Access granted")
        while True:
            # Receive commands from the client
            command = client_socket.recv(1024).decode().strip()

            # Handle the received command
            if command == "quit":
                client_socket.send(b"Goodbye!")
                break
            else:
                response = f"You sent the command: {command}"
                client_socket.send(response.encode())
    else:
        client_socket.send(b"Access denied")

    # Close the connection with the client
    client_socket.close()

while True:
    # Accept incoming connections
    client_socket, client_address = server_socket.accept()
    handle_client(client_socket, client_address)
