import socket

# create a socket connection using the nc command
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 1234)) # bind the connection to port 1234
s.listen(1) 
connection, address = s.accept()

# start an infinite loop until !quit is entered
while True:
    data = connection.recv(1024).decode()
    if not data: break
    if data == '!quit': break

    # print the received message
    print("Received message:", data)

    # write a message back to the server
    response = input("Enter a response: ")
    connection.sendall(response.encode())
    
# close the connection when the loop is finished
connection.close()
print("Connection closed.")
