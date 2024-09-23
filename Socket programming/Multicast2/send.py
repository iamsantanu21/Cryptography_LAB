import socket
import struct

MCAST_GRP_1 = '224.1.1.1'
MCAST_GRP_2 = '224.1.1.2'
MCAST_PORT_1 = 5005
MCAST_PORT_2 = 5006

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2) 

while True:
    group = input("Send message to Group 1 or Group 2 (1/2): ")
    message = input("Enter your message: ").encode()

    if group == '1':
        sock.sendto(message, (MCAST_GRP_1, MCAST_PORT_1))
        print(f"Message sent to Group 1: {MCAST_GRP_1}:{MCAST_PORT_1}")
    elif group == '2':
        sock.sendto(message, (MCAST_GRP_2, MCAST_PORT_2))
        print(f"Message sent to Group 2: {MCAST_GRP_2}:{MCAST_PORT_2}")
    else:
        print("Invalid group selection!")
