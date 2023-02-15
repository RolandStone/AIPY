import socket
import threading

HOST = 'YOUR_SERVER_IP'
PORT = 8080

def send_command(conn, command):
    # Encode the command into bytes and send it to the server
    conn.sendall(command.encode())
    # Receive the response from the server
    data = conn.recv(1024)
    # Decode the response into a string
    response = data.decode()
    # Print the response
    print(response)

def receive_response(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        response = data.decode()
        print(response)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    receive_thread = threading.Thread(target=receive_response, args=(s,))
    receive_thread.start()
    while True:
        # Read a command from the user
        command = input('$ ')
        # Send the command to the server
        send_command(s, command)
