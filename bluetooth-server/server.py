import socket
from getmac import get_mac_address as gma

server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
print(gma())
