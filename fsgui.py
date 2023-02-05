import tkinter as tk
import socket

class FileServer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("File Server")
        self.root.geometry("200x200")
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('localhost', 8000))
        self.server_socket.listen(5)
        self.create_widgets()

    def create_widgets(self):
        self.start_button = tk.Button(self.root, text="Start Server", command=self.start_server)
        self.start_button.pack()
        self.stop_button = tk.Button(self.root, text="Stop Server", command=self.stop_server)
        self.stop_button.pack()
        self.status_label = tk.Label(self.root, text="Server is not running.")
        self.status_label.pack()

    def start_server(self):
        self.status_label.config(text="Server is running.")
        while True:
            client_socket, client_address = self.server_socket.accept()
            client_socket.send("Thank you for connecting".encode())
            client_socket.close()

    def stop_server(self):
        self.status_label.config(text="Server is not running.")
        self.server_socket.close()
        self.root.destroy()

file_server = FileServer()
file_server.root.mainloop()

