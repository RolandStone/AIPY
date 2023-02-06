import tkinter as tk
from tkinter import filedialog
import subprocess
import os
from PIL import Image, ImageTk
def open_file():
    filepath = filedialog.askopenfilename()
    os.startfile(filepath)

def run_command():
    command = input("Enter command to run: ")
    subprocess.run(command, shell=True)

def open_directory():
    directory = filedialog.askdirectory()
    print(f"Opening directory: {directory}")

def create_new_desktop():
    # Create a new tkinter window
    new_desktop = tk.Tk()
    new_desktop.title("New Desktop")
    new_desktop.geometry("400x300")
    label = tk.Label(new_desktop, text="This is a new desktop")
    label.pack()
    # Add a folder icon
    folder_icon = tk.PhotoImage(file="folder_icon.png")
    folder_button = tk.Button(new_desktop, image=folder_icon, command=open_directory)
    folder_button.image = folder_icon
    folder_button.pack()

root = tk.Tk()
root.title("Desktop")

open_file_button = tk.Button(root, text="Open File", command=open_file)
open_file_button.pack()

run_command_button = tk.Button(root, text="Run Command", command=run_command)
run_command_button.pack()

open_directory_button = tk.Button(root, text="Open Directory", command=open_directory)
open_directory_button.pack()

create_new_desktop_button = tk.Button(root, text="New Desktop", command=create_new_desktop)
create_new_desktop_button.pack()

root.mainloop()
