import os
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

def list_files(path):
    files = os.listdir(path)
    for i, file in enumerate(files):
        listbox.insert(END, f"{i+1}. {file}")

def open_directory():
    index = listbox.curselection()
    if index:
        new_dir = os.path.join(cwd, listbox.get(index).split(".")[1].strip())
        if os.path.isdir(new_dir):
            cwd.set(new_dir)
            listbox.delete(0, END)
            list_files(cwd.get())
        else:
            messagebox.showerror("Error", f"{new_dir} is not a directory.")
    else:
        messagebox.showerror("Error", "No directory selected.")

def create_file():
    file_name = filedialog.asksaveasfilename(initialdir = cwd.get(), title = "Select file", filetypes = (("Text files", "*.txt"), ("all files", "*.*")))
    if file_name:
        try:
            open(file_name, "x").close()
            messagebox.showinfo("Info", f"{file_name} created.")
            listbox.delete(0, END)
            list_files(cwd.get())
        except FileExistsError:
            messagebox.showerror("Error", f"{file_name} already exists.")

def go_back():
    cwd.set(os.path.abspath(os.path.join(cwd.get(), os.pardir)))
    listbox.delete(0, END)
    list_files(cwd.get())

def quit():
    if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
        root.destroy()

root = Tk()
root.title("File Explorer")
root.geometry("400x300")

cwd = StringVar(value=os.getcwd())

Label(root, textvariable=cwd).pack()

listbox = Listbox(root)
listbox.pack()

list_files(cwd.get())

frame = Frame(root)
frame.pack()

Button(frame, text="Open", command=open_directory).pack(side=LEFT)
Button(frame, text="New", command=create_file).pack(side=LEFT)
Button(frame, text="Back", command=go_back).pack(side=LEFT)
Button(frame, text="Quit", command=quit).pack(side=LEFT)

root.mainloop()
