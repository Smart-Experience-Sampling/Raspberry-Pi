import socket

client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
# mac = input("Enter mac address: ")
client.connect(("ac:74:b1:87:2b:4c", 4))


try:
    while True:
        message = input("Enter message: ")
        client.send(message.encode("utf-8"))
        data = client.recv(1024)
        if not data:
            break

        print(f"Mesage: {data.decode('utf-8')}")

except OSError as e:
    print(f"Error: {e}")
