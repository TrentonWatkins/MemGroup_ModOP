import os
import socket
import threading

# RECEIVING FILELOC FROM PROC MGMT (SAVE IN MEM) > PARSING AND 
# SENDING TO STORAGE (PULL FROM MEM) > WAITING FOR RESPONSE > SENDING FILE TO PROC (STORE IN MEM B4)
# STAYING OPEN FOR FURTHER COMMUNICATION

# RECEIVING FILELOC FROM PROC MGMT
def recFromProc(host='0.0.0.0', port=1629):

    # Create a TCP socket for the server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the host and port
    server_socket.bind((host, port))
    
    # Start listening for incoming connections, with a backlog of 1 client
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    # Function to handle receiving a text message FROM PROCESS
    def receive_text(connection):
        # Receive the text message
        text = connection.recv(1024).decode()
        print(f"Received text: {text}")
        #!!!STORE IN MEM

    while True:
        # Accept an incoming connection from a client
        conn, addr = server_socket.accept()
        print(f"Connected to {addr}")

        # Receive the data type (either 'text' or 'file')
        data_type = conn.recv(1024).decode()
        
        # Handle the type of data received: text or file
        if data_type == 'text':
            receive_text(conn)
        else:
           print(f"Invalid data type recieved from PROCMGMT, expecting text; received: " {data_type})

        # Close the connection after handling the data
        conn.close()

# PARSING AND SENDING TO STORAGE
def sendToStor():


# RECEIVING FROM STORAGE
def recFromStor():


# SENDING TO PROCESS MGMT
def sendToProc():



# Start function to allow the user to choose between server or client mode
def memServer():
    cont = input("Open memory server? (y/n): ").strip().lower()
    
    # Run the appropriate mode based on user input
    if cont == "y":
        while True:
            recFromProc()
            sendToMem()
            recFromMem()
            sendToProc()

            cont = input("Loop? (y/n): ").strip().lower()

            if cont == "n":
                print(f"Ending program...")
                exit()

            else:
                # Handle invalid input
                print("Enter y or n...")

    elif cont == "n":
        print(f"Ending program...")
        exit()
    else:
        # Handle invalid input
        print("Enter y or n...")

# Entry point of the program
if __name__ == "__main__":
    # Start the bidirectional communication in a separate thread
    threading.Thread(target=memServer).start()
