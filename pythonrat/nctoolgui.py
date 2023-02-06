import os
import sys
import subprocess
from tkinter import *

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

def send_file_gui():
    file_path = file_path_entry.get()
    ip = ip_entry.get()
    port = int(port_entry.get())
    send_file(file_path, ip, port)

def receive_file_gui():
    file_path = file_path_entry.get()
    ip = ip_entry.get()
    port = int(port_entry.get())
    receive_file(file_path, ip, port)

def send_message_gui():
    message = message_entry.get()
    ip = ip_entry.get()
    port = int(port_entry.get())
    send_message(message, ip, port)

def receive_message_gui():
    ip = ip_entry.get()
    port = int(port_entry.get())
    received_message = receive_message(ip, port)
    message_label.config(text=received_message)

def print_help():
    print("Usage: python file_transfer.py [options]")
    print("Options:")
    print("-h, --help\t\t\tShow this help message")
    print("-s, --send\t\t\tSend a file")
    print("-r, --receive\t\tReceive a file")
    print("-i, --ip IP\t\t\tIP address of the host to connect to")
    print("-p, --port PORT\t\tPort to use for the connection")
    print("-f, --file FILE\t\tFile to send or receive")

if "-h" in sys.argv or "--help" in sys.argv:
    print_help()
    sys.exit()
root = Tk()
root.title("P2P File Sharing and Messaging")

file_path_label = Label(root, text="File Path:")
file_path_label.grid(row=0, column=0)
file_path_entry = Entry(root)
file_path_entry.grid(row=0, column=1)

ip_label = Label(root, text="IP Address:")
ip_label.grid(row=1, column=0)
ip_entry = Entry(root)
ip_entry.grid(row=1, column=1)

port_label = Label(root, text="Port:")
port_label.grid(row=2, column=0)
port_entry = Entry(root)
port_entry.grid(row=2, column=1)

send_file_button = Button(root, text="Send File", command=send_file_gui)
send_file_button.grid(row=3, column=0)

receive_file_button = Button(root, text="Receive File", command=receive_file_gui)
receive_file_button.grid(row=3, column=1)

Message
