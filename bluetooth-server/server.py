import socket
from getmac import get_mac_address as gma

server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
mac = gma()

server.bind((mac, 4))

server.listen(1)
client, addr = server.accept()

try:
    while True:
        data = client.recv()
        if not data:
            break
        print(f"Message: {data.decode('utf-8')}")
        message = input("Enter message: ")
        client.send(message.encode("utf-8"))
except OSError as e:
    print(f"Error: {e}")

client.close()
server.close()
