import socket

LHOST = input("Enter the listener IP address: ")
LPORT = int(input("Enter the listener port number: "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((LHOST, LPORT))
s.listen(1)
print(f"[*] Listening on {LHOST}:{LPORT}")

conn, addr = s.accept()
print(f"[*] Connection established with {addr[0]}:{addr[1]}")

while True:
    cmd = input("$ ")
    if cmd == "exit":
        break
    if len(cmd) > 0:
        conn.send(cmd.encode("utf-8"))
        result = conn.recv(1024).decode("utf-8")
        print(result, end="")

conn.close()
