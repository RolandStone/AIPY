import socket

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 1337))
    server_socket.listen(5)

    print("Server started. Waiting for clients...")
    client_socket, client_address = server_socket.accept()

    print("Client connected from:", client_address)

    username = client_socket.recv(1024).decode().strip()
    password = client_socket.recv(1024).decode().strip()

    if username == 'captain' and password == 'fckgwrhqq2':
        client_socket.sendall("Login successful!".encode())

        menu = "1. Fileserver\n2. Reverse Shell\n3. System Info\n4. Quit\n"
        client_socket.sendall(menu.encode())
        option = int(client_socket.recv(1024).decode().strip())

        if option == 1:
            client_socket.sendall("File server selected".encode())
        elif option == 2:
            client_socket.sendall("Reverse shell selected".encode())
        elif option == 3:
            system_info = "This is the system info"
            client_socket.sendall("System info selected".encode())
            client_socket.sendall(system_info.encode())
        elif option == 4:
            client_socket.sendall("Quit selected".encode())
        else:
            client_socket.sendall("Invalid option".encode())

        client_socket.close()
    else:
        client_socket.sendall("Login failed".encode())
        client_socket.close()
        
    server_socket.close()

def run_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('0.0.0.0', 1337))

    username = 'captain'
    password = 'fckgwrhqq2'

    client_socket.sendall(username.encode())
    client_socket.sendall(password.encode())

    response = client_socket.recv(1024).decode().strip()
    if response == 'Login successful!':
        print(response)
        menu = client_socket.recv(1024).decode().strip()
        print(menu)
        option = int(input('Enter your option: '))
        client_socket.sendall(str(option).encode())

        if option in [1, 2, 3]:
            response = client_socket.recv(1024).decode().strip()
            print(response)
            if option == 3:
                system_info = client_socket.recv(1024).decode().strip()
                print(system_info)
        else:
            response = client_socket.recv(1024).decode().strip()
            print(response)

    else:
        print(response)
