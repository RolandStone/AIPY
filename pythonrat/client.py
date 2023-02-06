import socket
import subprocess

def start_client(server_host, server_port):
    # Connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))
    print(f'Connected to {server_host}:{server_port}')

    while True:
        # Read a command from the user
        command = input('$ ')

        # Send the command to the server
        client_socket.send(command.encode())

        # Receive the response from the server
        response = client_socket.recv(4096).decode()

        # Print the response
        print(response)

if __name__ == '__main__':
    start_client('10.0.0.214', 1337)
