import socket

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

    if option == 1:
        # ... file server code ...
    elif option == 2:
        # ... reverse shell code ...
    elif option == 3:
        response = client_socket.recv(1024).decode().strip()
        print(response)
        system_info = client_socket.recv(1024).decode().strip()
        print(system_info)
    elif option == 4:
        response = client_socket.recv(1024).decode().strip()
        print(response)
    else:
        response = client_socket.recv(1024).decode().strip()
        print(response)
else:
    print(response)

client_socket.close()
