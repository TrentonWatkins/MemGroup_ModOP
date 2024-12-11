import os
import socket

# Function to receive the fileLocation on port 1629 and append it to "read/"
def receive_file_location():
    host = '0.0.0.0'  # Listen on all available network interfaces
    port_location = 1629  # Port to receive fileLocation string
    port_file = 12345      # Port to receive file data

    # Create a TCP socket to receive the fileLocation
    location_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    location_socket.bind((host, port_location))
    location_socket.listen(1)
    print(f"Server listening for file location on port {port_location}...")

    # Accept connection for receiving fileLocation string
    conn_location, addr_location = location_socket.accept()
    print(f"Connected to {addr_location} to receive file location.")

    try:
        # Receive the fileLocation string
        file_location = conn_location.recv(1024).decode()  # Receive up to 1024 bytes
        print(f"Received file location: {file_location}")

        # Append the fileLocation to the string "read/"
        stor_msg = "read/" + file_location
        print(f"Constructed storMsg: {stor_msg}")

    except Exception as e:
        print(f"Error receiving file location: {e}")
        stor_msg = None  # If there's an error, set storMsg to None
    
    # Close the connection after receiving fileLocation
    conn_location.close()

    # If storMsg is constructed, proceed to receive the file on port 12345
    if stor_msg:
        receive_file(stor_msg, port_file)

# Function to receive the file and save it using storMsg path
def receive_file(stor_msg, port_file):
    # Create a TCP socket to receive the file
    file_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    file_socket.bind(('0.0.0.0', port_file))
    file_socket.listen(1)
    print(f"Waiting to receive the file on port {port_file}...")

    # Accept the connection for receiving the file
    conn_file, addr_file = file_socket.accept()
    print(f"Connected to {addr_file} to receive file.")

    try:
        # Receive the file name and size
        file_name = conn_file.recv(1024).decode()
        file_size = int(conn_file.recv(1024).decode())
        print(f"Receiving file: {file_name} (size: {file_size} bytes)")

        # Create the full file path with storMsg
        file_path = os.path.join(stor_msg, file_name)

        # Create the directory for the file if it doesn't exist
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Open the file for writing in binary mode
        with open(file_path, 'wb') as file:
            received = 0
            while received < file_size:
                data = conn_file.recv(1024)
                file.write(data)
                received += len(data)
        
        print(f"File received and saved as {file_path}")

    except Exception as e:
        print(f"Error receiving file: {e}")

    # Close the file connection
    conn_file.close()

# Entry point of the program
if __name__ == "__main__":
    receive_file_location()
