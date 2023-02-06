import socketserver

class IRCRequestHandler(socketserver.StreamRequestHandler):
    def handle(self):
        nickname = None
        while True:
            self.data = self.rfile.readline().strip().decode()
            if not self.data:
                break
            print(f"Received message: {self.data}")

            # handle Nick command
            if self.data.startswith("NICK"):
                nickname = self.data.split()[1]
                self.wfile.write(f"001 {nickname} :Welcome to the IRC server!\n".encode())
                continue

            # handle User command
            if self.data.startswith("USER"):
                self.wfile.write(f"002 {nickname} :User registered\n".encode())
                continue

            # handle Join command
            if self.data.startswith("JOIN"):
                channel = self.data.split()[1]
                self.wfile.write(f"003 {nickname} :joined {channel}\n".encode())
                continue

            # handle Privmsg command
            if self.data.startswith("PRIVMSG"):
                recipient, message = self.data.split(" ", 2)[1:]
                self.wfile.write(f"004 {nickname} :{recipient} {message}\n".encode())
                continue

            self.wfile.write(b"Unknown command\n")

server = socketserver.TCPServer(("", 6667), IRCRequestHandler)
server.serve_forever()
