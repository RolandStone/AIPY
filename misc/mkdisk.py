import os

def create_file():
    filename = input("Enter the file name: ")
    size = input("Enter the file size in MB: ")
    format = input("Enter the file format (e.g. '.txt', '.pdf'): ")

    full_filename = filename + format
    os.system(f"dd if=/dev/zero of={full_filename} bs=1MB count={size}")
    print(f"{full_filename} has been created.")

if __name__ == "__main__":
    create_file()

