import socket

def start_server():
    """Starts the server and listens for incoming client connections"""
    host = ""
    port = 12345

    # create a TCP/IP socket
    s = socket.socket()

    # bind the socket to a specific address and port
    s.bind((host, port))

    # listen for incoming connections
    s.listen()

    print(f"[+] Server started at {host}:{port}")

    # wait for a connection
    conn, addr = s.accept()
    print(f"[+] Client connected from {addr[0]}:{addr[1]}")

    # send a welcome message to the client
    conn.send("Welcome to the chatroom!".encode())

    while True:
        # receive data from the client
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"Client: {data}")

        # send data back to the client
        message = input("You: ")
        if message.startswith("SEND"):
            filename = message.split()[1]
            send_file(filename, conn)
        elif message.startswith("GET"):
            filename = message.split()[1]
            receive_file(filename, conn)
        else:
            conn.send(message.encode())

    # close the connection
    conn.close()

def start_client():
    """Starts the client and connects to a server"""
    host = input("Enter server address: ")
    port = int(input("Enter port: "))

    # create a TCP/IP socket
    s = socket.socket()

    # connect to the server
    s.connect((host, port))
    print("[+] Connected to server")

    # receive the welcome message from the server
    data = s.recv(1024).decode()
    print(f"Server: {data}")

    while True:
        # receive data from the server
        message = input("You: ")
        if message.startswith("SEND"):
            filename = message.split()[1]
            send_file(filename, s)
        elif message.startswith("GET"):
            filename = message.split()[1]
            receive_file(filename, s)
        else:
            s.send(message.encode())
            data = s.recv(1024).decode()
            if not data:
                break
            print(f"Server: {data}")

    # close the connection
    s.close()

def send_file(filename, conn):
    """Sends a file to the specified connection"""
    with open(filename, "rb") as f:
        data = f.read()
        conn.send(data)

def receive_file(filename, conn):
    """Receives a file from the specified connection"""
    with open(filename, "wb") as f:
        data = conn.recv(1024)
        f.write(data)

if __name__ == '__main__':
    # ask the user if they want to start as a server or client
    mode = input("Would you like to start as a server or client? (Enter 'server' or 'client'): ")
if mode.lower() == "server":
	start_server()
elif mode.lower() == "client":
	start_client()
else:
	print("Invalid choice, try again.")
