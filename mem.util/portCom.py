import os
import socket
import threading


# Server setup
def server_mode(host='0.0.0.0', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    def receive_file(connection):
        file_name = connection.recv(1024).decode()
        file_size = connection.recv(1024).decode()

        with open(file_name, 'wb') as file:
            received = 0
            while received < int(file_size):
                data = connection.recv(1024)
                file.write(data)
                received += len(data)
        print(f"File {file_name} received successfully.")

    def receive_text(connection):
        text = connection.recv(1024).decode()
        print(f"Received text: {text}")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connected to {addr}")

        data_type = conn.recv(1024).decode()  # 'text' or 'file'
        
        if data_type == 'text':
            receive_text(conn)
        elif data_type == 'file':
            receive_file(conn)

        conn.close()

# Client setup
def client_mode(server_ip, server_port=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    def send_text(text):
        client_socket.sendall(b'text')
        client_socket.sendall(text.encode())
        print(f"Sent text: {text}")

    def send_file(file_path):
        client_socket.sendall(b'file')
        file_name = os.path.basename(file_path)
        file_size = os.path.getsize(file_path)

        client_socket.sendall(file_name.encode())
        client_socket.sendall(str(file_size).encode())

        with open(file_path, 'rb') as file:
            while (data := file.read(1024)):
                client_socket.sendall(data)
        print(f"File {file_name} sent successfully.")

    # Example usage
    option = input("Send text or file? (text/file): ").strip()

    if option == "text":
        text = input("Enter the text to send: ")
        send_text(text)
    elif option == "file":
        file_path = input("Enter the file path: ").strip()
        send_file(file_path)

    client_socket.close()

def start_bidirectional():
    mode = input("Run as server or client? (server/client): ").strip().lower()
    if mode == "server":
        server_mode()
    elif mode == "client":
        server_ip = input("Enter the server IP address: ").strip()
        client_mode(server_ip)
    else:
        print("Invalid mode. Please enter 'server' or 'client'.")

if __name__ == "__main__":
    threading.Thread(target=start_bidirectional).start()
