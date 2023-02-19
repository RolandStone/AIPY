import socket
import subprocess
import os

def connect(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        return s
    except Exception as e:
        print("Error: ", e)
        return None

def send_command(s, command):
    try:
        s.send(command.encode())
        output = s.recv(1024).decode()
        if "cd " in command:
            return ""
        return output
    except Exception as e:
        print("Error: ", e)
        return ""

def main():
    ip = input("Enter the server IP address or https url: ")
    port = int(input("Enter the port number: "))
    s = connect(ip, port)

    while True:
        command = input("> ")
        if command == "exit":
            send_command(s, "exit")
            s.close()
            break
        elif command == "background":
            pid = os.fork()
            if pid == 0:
                while True:
                    command = input("> ")
                    if command == "resume":
                        break
                    elif command == "exit":
                        send_command(s, "exit")
                        s.close()
                        os._exit(0)
                    else:
                        output = send_command(s, command)
                        if output:
                            print(output)
                os._exit(0)
        else:
            output = send_command(s, command)
            if output:
                print(output)

if __name__ == "__main__":
    main()
