import socket

def start_server():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    server_address = ('localhost', 12345)
    print('Starting up tunnel on %s port %s' % server_address)
    server_socket.bind(server_address)

    # Listen for incoming connections
    server_socket.listen(1)

    while True:
        # Wait for a connection
        print('Waiting for a connection...')
        client_socket, client_address = server_socket.accept()
        print('Accepted connection from %s:%s' % client_address)

        # Receive data from the client
        data = client_socket.recv(1024)

        # Send the data back to the client
        client_socket.sendall(data)

        # Clean up the connection
        client_socket.close()
        print('Connection closed.')

if __name__ == '__main__':
    start_server()
