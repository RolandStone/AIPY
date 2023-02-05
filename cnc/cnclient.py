import socket

# Ask the user for the IP address and port of the server
server_ip = input("Enter the IP address of the server: ")
server_port = int(input("Enter the port of the server: "))

# Connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

# Ask the user for their username and password
username = input("Enter your username: ")
password = input("Enter your password: ")

# Send the username and password to the server
client_socket.send(username.encode())
client_socket.send(password.encode())

# Receive the result of the login attempt from the server
result = client_socket.recv(1024).decode().strip()
print(result)

# Continue to ask the user for commands if the login was successful
if result == "Access granted":
    while True:
        command = input("Enter a command (type 'quit' to exit): ")
        if command == "quit":
            break
        client_socket.send(command.encode())
        response = client_socket.recv(1024).decode().strip()
        print(response)

# Close the connection with the server
client_socket.close()

