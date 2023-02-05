import os

def list_files(path):
    files = os.listdir(path)
    for i, file in enumerate(files):
        print(f"{i+1}. {file}")

def main():
    cwd = os.getcwd()
    while True:
        # Print the current working directory
        print("\nCurrent working directory:", cwd)

        # List the files in the current directory
        list_files(cwd)

        # Ask the user for their choice
        choice = input("\nEnter number to open directory, N to create new file, B to go back, Q to quit: ")

        # Check if the choice is a number
        try:
            choice = int(choice)
            # Check if the number is within range
            if 1 <= choice <= len(os.listdir(cwd)):
                # Change directory
                new_dir = os.path.join(cwd, os.listdir(cwd)[choice-1])
                if os.path.isdir(new_dir):
                    cwd = new_dir
                else:
                    print(f"{new_dir} is not a directory.")
            else:
                print("Invalid choice.")
        except ValueError:
            if choice.upper() == "N":
                # Create a new file
                file_name = input("Enter the name of the new file: ")
                try:
                    open(os.path.join(cwd, file_name), "x").close()
                    print(f"{file_name} created.")
                except FileExistsError:
                    print(f"{file_name} already exists.")
            elif choice.upper() == "B":
                # Go back
                cwd = os.path.abspath(os.path.join(cwd, os.pardir))
            elif choice.upper() == "Q":
                # Quit
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    main()

