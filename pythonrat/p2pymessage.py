import socket
import sys

def send_message(ip, port, message):
    # Create a socket and send the message
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip, port))
    client_socket.sendall(message.encode())
    client_socket.close()

def receive_message(ip, port):
    # Create a socket and receive the message
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip, port))
    server_socket.listen()
    connection, address = server_socket.accept()
    message = connection.recv(4096).decode()
    connection.close()
    server_socket.close()
    return message

def display_help_menu():
    print("Usage: python <script_name>.py <command> <ip> <port> <message>")
    print("Commands:")
    print("\tsend\t\tSends a message to the specified IP address and port")
    print("\treceive\t\tReceives a message from the specified IP address and port")
    print("\thelp\t\tDisplays this help menu")

# Main program
if __name__ == '__main__':
    if len(sys.argv) < 2:
        display_help_menu()
        sys.exit(1)

    command = sys.argv[1]
    if command == 'send':
        if len(sys.argv) < 5:
            print("Error: Missing arguments.\n")
            display_help_menu()
            sys.exit(1)
        ip = sys.argv[2]
        port = int(sys.argv[3])
        message = sys.argv[4]
        send_message(ip, port, message)
    elif command == 'receive':
        if len(sys.argv) < 4:
            print("Error: Missing arguments.\n")
            display_help_menu()
            sys.exit(1)
        ip = sys.argv[2]
        port = int(sys.argv[3])
        print(receive_message(ip, port))
    elif command == 'help':
        display_help_menu()
    else:
        print("Error: Invalid command.\n")
        display_help_menu()
        sys.exit(1)
