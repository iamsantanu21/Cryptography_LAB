import socket

def start_client():
    # AF_INET specifies IPv4, SOCK_STREAM specifies TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    # Connect to the server
    client_socket.connect(('localhost', 4000))
    print("Connected to the server.")

    while True:
        # Send data to the server
        message = input("Enter your message (or type 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        
        client_socket.send(message.encode('utf-8'))

        # Receive response from the server
        server_response = client_socket.recv(1024).decode('utf-8')
        print(f"Server: {server_response}")
    
    client_socket.close()

if __name__ == "__main__":
    start_client()
