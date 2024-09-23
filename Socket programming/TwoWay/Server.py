import socket

def start_server():
    # AF_INET specifies IPv4, SOCK_STREAM specifies TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    # Bind the server to the local host and a specific port
    server_socket.bind(('localhost', 4000))
    
    # Start listening for connections (max 5 queued connections)
    server_socket.listen(5)
    print("Server started and listening on port 5000.")

    while True:
        # Accept a connection
        client_socket, client_address = server_socket.accept()
        print(f"Client {client_address} connected.")
        
        # Communicate with the client
        while True:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                print(f"Client {client_address} disconnected.")
                break
            
            print(f"Client: {data}")
            server_message = input("Enter your message: ")
            client_socket.send(server_message.encode('utf-8'))
        
        client_socket.close()

if __name__ == "__main__":
    start_server()
