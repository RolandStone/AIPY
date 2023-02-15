import socket
import subprocess

def start_shell(conn):
    while True:
        # Receive data from the client
        data = conn.recv(1024)
        # Decode the data into a string
        data_string = data.decode()
        # Run the command and get the output
        output = subprocess.getoutput(data_string)
        # Encode the output into bytes and send it back to the client
        conn.sendall(output.encode())

host = input("Enter the host IP to listen on (e.g. 0.0.0.0): ")
port = int(input("Enter the port to listen on (e.g. 8080): "))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    print(f'Listening on {host}:{port}...')
    conn, addr = s.accept()
    with conn:
        print(f'Accepted connection from {addr}')
        start_shell(conn)
