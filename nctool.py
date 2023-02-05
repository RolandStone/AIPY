import os
import subprocess

# Send a file
def send_file(file_path, ip, port):
    with open(file_path, 'rb') as f:
        subprocess.run(["nc", ip, str(port)], stdin=f)

# Receive a file
def receive_file(file_path, ip, port):
    with open(file_path, 'wb') as f:
        subprocess.run(["nc", ip, str(port)], stdout=f)

# Send a message
def send_message(message, ip, port):
    subprocess.run(["nc", ip, str(port)], input=message.encode())

# Receive a message
def receive_message(ip, port):
    result = subprocess.run(["nc", "-l", str(port)], capture_output=True)
    return result.stdout.decode()

# Get IP and port from user
ip = input("Enter the IP address: ")
port = int(input("Enter the port number: "))

# Example usage
#send_file("example.txt", ip, port)
#receive_file("received_file.txt", ip, port)
send_message("Hello", ip, port)
print(receive_message(ip, port))

