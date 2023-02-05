import socket
import os

def send_file(filename, conn):
    if os.path.isfile(filename):
        filesize = os.path.getsize(filename)
        conn.send(f"EXISTS {filesize}".encode())
        response = conn.recv(1024).decode()
        if response[:2] == 'OK':
            with open(filename, 'rb') as f:
                bytes_to_send = f.read(1024)
                conn.send(bytes_to_send)
                while bytes_to_send != "":
                    bytes_to_send = f.read(1024)
                    conn.send(bytes_to_send)
    else:
        conn.send("ERR".encode())

def receive_file(filename, conn):
    response = conn.recv(1024).decode()
    if response[:6] == 'EXISTS':
        filesize = int(response[6:])
        conn.send("OK".encode())
        with open(filename, 'wb') as f:
            data = conn.recv(1024)
            total_received = len(data)
            f.write(data)
            while total_received < filesize:
                data = conn.recv(1024)
                total_received += len(data)
                f.write(data)
            print("File received successfully")
    else:
        print("File does not exist")

def handle_client(conn, addr):
    print(f"[+] New client connected from {addr[0]}:{addr[1]}")
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        if data.startswith("SEND"):
            filename = data.split()[1]
            send_file(filename, conn)
        elif data.startswith("GET"):
            filename = data.split()[1]
            receive_file(filename, conn)
        else:
            print(f"Client({addr[0]}:{addr[1]}): {data}")
            message = input("You: ")
            conn.send(message.encode())
    print(f"[-] Client disconnected from {addr[0]}:{addr[1]}")
    conn.close()

def start_server():
    host = '0.0.0.0'
    port = 5000

    s = socket.socket()
    s.bind((host, port))
    s.listen(1)
    print("[+] Server started")
    conn, addr = s.accept()
    print(f"[+] Client connected from {addr[0]}:{addr[1]}")
    handle_client(conn, addr)
    s.close()

if __name__ == '__main__':
    start_server()
