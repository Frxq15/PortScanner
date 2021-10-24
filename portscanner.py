import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(5)

host = ("10.6.119.128")
port = int(input("Please enter a port to scan: "))

def scan(port):
    if sock.connect_ex((host, port)):
        print("The port specified is closed for this IP address.")
    else:
        ("The port specified is open")

scan(port)
