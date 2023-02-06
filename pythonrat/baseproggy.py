import socket
import subprocess
import webbrowser

def chat_with_server(host, port):
    with socket.socket() as s:
        s.connect((host, port))

        message = input("-> ")
        while message.lower().strip() != 'bye':
            s.send(message.encode())
            data = s.recv(1024).decode()
            print("Received from server: " + data)
            message = input("-> ")

def start_reverse_connection(host, port):
    with socket.socket() as s:
        s.connect((host, port))
        print("Connected to server.")

def open_file_browser():
    subprocess.call(["explorer.exe"])

def main():
    print("Please select an option:")
    print("1. Open file browser")
    print("2. Chat with server")
    print("3. Start reverse connection")

    choice = int(input("Enter your choice (1-3): "))

    if choice == 1:
        open_file_browser()
    elif choice == 2:
        host = input("Enter the server hostname or IP address: ")
        port = int(input("Enter the server port number: "))
        chat_with_server(host, port)
    elif choice == 3:
        host = input("Enter the server hostname or IP address: ")
        port = int(input("Enter the server port number: "))
        start_reverse_connection(host, port)
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
