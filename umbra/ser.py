import serial.tools.list_ports
import requests
import time
from datetime import datetime
import json

# ports = serial.tools.list_ports.comports()
__BAUDRATE__ = 115200
__PORT__ = "COM3"
__API_URL__ = "http://localhost:5000/"
serial_inst = serial.Serial(baudrate=__BAUDRATE__, port=__PORT__)


def decode(data):
    bits = 32
    target = int(data[:bits], 2)
    num_beacons = int(str(data[: bits * 2])[bits:], 2)
    uuid = int(str(data[: bits * 3])[bits * 2 :], 2)
    timestamp = int(str(data[: bits * 4])[bits * 3 :], 2)
    # print(str(data[:bits*4])[bits*3:])

    beacons = []

    x = 4
    for i in range(num_beacons):
        uuid_b = int(str(data[: bits * (x + 1)])[bits * x :], 2)
        x += 1
        tof = int(str(data[: bits * (x + 1)])[bits * x :], 2)
        x += 1

        beacons.append({"uuid": uuid_b, "tof": tof})

    return {
        "target": target,
        "num_beacons": num_beacons,
        "uuid": uuid,
        "timestamp": timestamp,
        "beacons": beacons,
    }


while True:
    value = str(serial_inst.readline())

    if value is not None and value != "":
        # print(value)
        try:
            x = value.decode()
        except:
            x = value
        val = []
        temp = ""
        y = 0
        for v in x:

            y += 1
            if y <= 6:
                continue
            if v == " ":
                print("APPENDING")
                val.append(temp)
                temp = ""
            print(repr(v))

            temp += v
        # val = val.decode().split(" ")
        print(val)
        beacons = []

        num = int(int(val[0]) / 10)

        # print(meter, int(val[10]), int(val[i+11]), "+ meter ",  centimeter)

        # beacons.append({"beacon_id": beacon_id, "centimeter": centimeter})
        for i in range(num):
            beacon_id = (
                val[(i * 10) + 1]
                + val[(i * 10) + 2]
                + val[(i * 10) + 3]
                + val[(i * 10) + 4]
                + val[(i * 10) + 5]
                + val[(i * 10) + 6]
                + val[(i * 10) + 7]
                + val[(i * 10) + 8]
            )
            meter = int(val[(i * 10) + 9]) * 100
            centimeter = int(val[(i * 10) + 10]) + meter

            print(
                meter,
                int(val[(i * 10) + 9]),
                int(val[(i * 10) + 10]),
                "+ meter ",
                centimeter,
            )

            beacons.append({"beacon_id": beacon_id, "centimeter": centimeter})

        data_dict = {"beacon_num": num, "beacons": beacons}

        requests.post(f"{__API_URL__}click", json=data_dict)

        # Either in json, data or body. Either as string or as a dict

    time.sleep(0.1)
