import socket

def get_config():
    host = input('Enter the host address of the server: ')
    port = int(input('Enter the port of the server: '))
    return (host, port)

def main():
    server_address = get_config()

    # Create a TCP/IP socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the server's address and port
    client.connect(server_address)

    # Receive the options from the server
    options = b''
    while True:
        data = client.recv(1024)
        if not data:
            break
        options += data

    print('Received options from the server:')
    print(options.decode())

    # Choose an option
    choice = int(input('Enter your choice: '))
    client.sendall(str(choice).encode())

    # Receive the result from the server
    result = b''
    while True:
        data = client.recv(1024)
        if not data:
            break
        result += data

    print('Received result from the server:')
    print(result.decode())

    # Clean up the connection
    client.close()

if __name__ == '__main__':
    main()
