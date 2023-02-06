import paramiko

# Get the host address, username, and password from the user
host_address = input("Enter the host address: ")
username = input("Enter the username: ")
password = input("Enter the password: ")

# Create an SSH client object
ssh_client = paramiko.SSHClient()

# Automatically add the server's host key (recommended for security)
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the remote server
ssh_client.connect(hostname=host_address, username=username, password=password)

# Start the SSH tunnel
transport = ssh_client.get_transport()
dest_addr = ("localhost", 1337)
local_addr = ("localhost", 1337)
channel = transport.open_channel("direct-tcpip", dest_addr, local_addr)

# Keep the tunnel alive until the user types "escape!"
while True:
    command = input("Enter a command (or type 'escape!' to exit): ")
    if command == "escape!":
        break
    # Use the tunnel
    # ...

# Close the tunnel
channel.close()
ssh_client.close()
