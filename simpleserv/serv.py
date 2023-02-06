import socket
import subprocess

users = {'captain': 'fckgwrhqq2'}

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 1337))
server_socket.listen(1)

print('Server listening on 0.0.0.0:1337...')

while True:
    client_socket, client_address = server_socket.accept()
    print(f'Accepted connection from {client_address[0]}:{client_address[1]}')

    username = client_socket.recv(1024).decode().strip()
    password = client_socket.recv(1024).decode().strip()

    if username in users and users[username] == password:
        client_socket.sendall(b'Login successful!')

        menu = """
        Welcome, {}! Please choose an option:
        1. File Server
        2. Reverse Shell
        3. Send System Info
        4. Log out
        """.format(username)

        client_socket.sendall(menu.encode())

        option = int(client_socket.recv(1024).decode().strip())

        if option == 1:
            # ... file server code ...
        elif option == 2:
            # ... reverse shell code ...
        elif option == 3:
            client_socket.sendall(b'You selected option 3: Send System Info')
            system_info = subprocess.check_output('uname -a', shell=True)
            client_socket.sendall(system_info)
        elif option == 4:
            client_socket.sendall(b'Logging out...')
        else:
            client_socket.sendall(b'You selected option {}'.format(option))

    else:
        client_socket.sendall(b'Login failed. Incorrect username or password.')

    client_socket.close()
