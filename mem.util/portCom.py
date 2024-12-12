import os
import socket
import threading

import priProc

memory_heap1 = []
memory_heap2 = []
memory_heap3 = []
# Server setup function to handle incoming connections and file/text transfer
def server_mode(host='0.0.0.0'):

    group = input("Receiving from storage or process? (storage/process): ").strip().lower()
    
    # Opened port will depend on the group sending the file
    if group == "storage":
        port = 99887
    elif group == "process":
        port = 1629
    else:
        # Handle invalid input
        print("Invalid group. Please enter 'storage' or 'process'.")

    # Create a TCP socket for the server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the host and port
    server_socket.bind((host, port))
    
    # Start listening for incoming connections, with a backlog of 1 client
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    # Function to handle receiving a file FROM STORAGE
    def receive_file(connection):
        # Receive the file name and size
        file_name = connection.recv(1024).decode()
        file_size = connection.recv(1024).decode()

        # Open a file to write the incoming data
        with open(file_name, 'wb') as file:
            received = 0
            # Receive the file in chunks and write it to the file until the entire file is received
            while received < int(file_size):
                data = connection.recv(1024)
                file.write(data)
                received += len(data)
        print(f"File {file_name} received successfully.")
        priProc.replaceMemBlock(memory_heap1, file_name)

    # Function to handle receiving a text message FROM PROCESS
    def receive_text(connection):
        # Receive the text message
        text = connection.recv(1024).decode()
        print(f"Received text: {text}")
        priProc.replaceMemBlock(memory_heap1, text)

    while True:
        # Accept an incoming connection from a client
        conn, addr = server_socket.accept()
        print(f"Connected to {addr}")

        # Receive the data type (either 'text' or 'file')
        data_type = conn.recv(1024).decode()
        
        # Handle the type of data received: text or file
        if data_type == 'text':
            receive_text(conn)
        elif data_type == 'file':
            receive_file(conn)

        # Close the connection after handling the data
        conn.close()

# Client setup function to send text or file to the server
def client_mode(server_ip):

    group = input("Sending to storage or process? (storage/process): ").strip().lower()
    
    # Server port will depend on the group receiving the file/text
    if group == "storage":
        server_port = 12345
    elif group == "process":
        server_port = 54321
    else:
        # Handle invalid input
        print("Invalid group. Please enter 'storage' or 'process'.")

    # Create a TCP socket for the client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the server at the provided IP and port
    client_socket.connect((server_ip, server_port))

    # Function to send a text message TO STORAGE
    def send_text(text):
        # Indicate that the data type is 'text'
        client_socket.sendall(b'text')
        
        # Send the actual text message
        client_socket.sendall(text.encode())
        print(f"Sent text: {text}")

    # Function to send a file to PROCESS 
    def send_file(file_path):
        # Indicate that the data type is 'file'
        client_socket.sendall(b'file')
        
        # Get the file name and size
        file_name = os.path.basename(file_path)
        file_size = os.path.getsize(file_path)

        # Send the file name and size
        client_socket.sendall(file_name.encode())
        client_socket.sendall(str(file_size).encode())

        # Open the file and send it in chunks to the server
        with open(file_path, 'rb') as file:
            while (data := file.read(1024)):
                client_socket.sendall(data)
        print(f"File {file_name} sent successfully.")

    # Prompt user to choose whether to send text or file
    option = input("Send text or file? (text/file): ").strip()

    # Depending on the user's choice, either send text or file
    if option == "text":
        text = input("Enter the text to send: ")
        send_text(text)
    elif option == "file":
        file_path = input("Enter the file path: ").strip()
        send_file(file_path)

    # Close the connection after sending data
    client_socket.close()

# Start function to allow the user to choose between server or client mode
def start_bidirectional():
    mode = input("Run as server or client? (server/client): ").strip().lower()
    
    # Run the appropriate mode based on user input
    if mode == "server":
        server_mode()
    elif mode == "client":
        server_ip = input("Enter the server IP address: ").strip()
        client_mode(server_ip)
    else:
        # Handle invalid input
        print("Invalid mode. Please enter 'server' or 'client'.")

# Entry point of the program
if __name__ == "__main__":
    # Start the bidirectional communication in a separate thread
    threading.Thread(target=start_bidirectional).start()
