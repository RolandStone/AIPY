import tkinter as tk
import os

def create_file():
    file_name = file_name_entry.get()
    file_size = int(file_size_entry.get())
    file_format = file_format_entry.get()
    file_location = file_location_entry.get()

    file_path = os.path.join(file_location, file_name + file_format)

    file_size_bytes = file_size * 1024 * 1024 * 1024

    with open(file_path, "wb") as f:
        f.write(b"0" * file_size_bytes)

    result_label.config(text="File created successfully at: " + file_path)

root = tk.Tk()
root.title("File Creator")

file_name_label = tk.Label(root, text="Enter the file name: ")
file_name_label.grid(row=0, column=0)

file_name_entry = tk.Entry(root)
file_name_entry.grid(row=0, column=1)

file_size_label = tk.Label(root, text="Enter the file size in GB: ")
file_size_label.grid(row=1, column=0)

file_size_entry = tk.Entry(root)
file_size_entry.grid(row=1, column=1)

file_format_label = tk.Label(root, text="Enter the file format (e.g., '.txt', '.pdf'): ")
file_format_label.grid(row=2, column=0)

file_format_entry = tk.Entry(root)
file_format_entry.grid(row=2, column=1)

file_location_label = tk.Label(root, text="Enter the output location for the file: ")
file_location_label.grid(row=3, column=0)

file_location_entry = tk.Entry(root)
file_location_entry.grid(row=3, column=1)

create_button = tk.Button(root, text="Create File", command=create_file)
create_button.grid(row=4, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=2)

root.mainloop()
