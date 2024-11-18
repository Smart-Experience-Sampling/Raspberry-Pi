import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
serial_inst = serial.Serial()

port_list = []

i = 1
for port in ports:
	port_list.append(str(port))
	print(f"{i}. {str(port)}")
	i += 1

val = int(input("Select Port: "))
# print(f"Selected com port -> {}")

serial_inst.baudrate = 9600
serial_inst.port = port_list[val-1]
serial_inst.open()