import random
import time

sample_str = "000000000000000000000000000000010000000000000000000000000000001050b7a067-f55e-4fe3-ac64-bc0e65f7011001110011111001101110110001012c4f3a59-26a6-4347-9c58-3e45f96a00000000000000000000001001011000620f3499-c28e-483d-b3fb-d3ef34db00000000000000000000001001011101"



def current_milli_time():
    return round(time.time() * 1000)

def decode(data):
    bits = 32
    target = int(data[:bits], 2)
    num_beacons = int(str(data[:bits*2])[bits:], 2)
    uuid = int(str(data[:bits*3])[bits*2:], 2)
    timestamp = int(str(data[:bits*4])[bits*3:], 2)
    # print(str(data[:bits*4])[bits*3:])

    beacons = []

    x = 4
    for i in range(num_beacons):
        uuid_b = int(str(data[:bits*(x+1)])[bits*x:], 2)
        x += 1
        tof = int(str(data[:bits*(x+1)])[bits*x:], 2)
        x += 1

        beacons.append({"uuid": uuid_b, "tof": tof})

    return {"target": target, "num_beacons": num_beacons, "uuid": uuid, "timestamp": timestamp, "beacons": beacons}

def test(num):
    passed = 0
    failed = 0
    for i in range(num):
        target = random.randint(0, 4_294_967_000)
        num_beacons = random.randint(0, 200)
        uuid = random.randint(0, 4_294_967_000)
        timestamp = random.randint(0, 4_294_967_000)
        decode_str = "{:032b}".format(target)
        decode_str += "{:032b}".format(num_beacons)
        decode_str += "{:032b}".format(uuid)
        decode_str += "{:032b}".format(timestamp)

        beacons = []
        for beacon in range(num_beacons):
            uuid_b = random.randint(0, 4_294_967_000)
            tof = random.randint(0, 10000)
            beacons.append({"uuid": uuid_b, "tof": tof})
            decode_str += "{:032b}".format(uuid_b)
            decode_str += "{:032b}".format(tof)

        ret_val = decode(decode_str)
        try: 
            assert(int(ret_val['target']) == target)
            assert(int(ret_val['num_beacons']) == num_beacons)
            assert(int(ret_val['uuid']) == uuid)
            assert(int(ret_val['timestamp']) == timestamp)
            assert(ret_val['beacons'] == beacons)
            passed += 1
        except AssertionError as e:
            print(e)
            failed += 1

        print(f"Ran {(i+1):_}/{num:_}", end="\r")

    print(f"Passed: {passed:_}/{num:_}")
    print(f"Failed: {failed:_}/{num:_}")

test(100_000)