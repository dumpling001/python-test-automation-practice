devices = [
    {"id": "A001", "voltage": 3.3},
    {"id": "A002", "voltage": 3.0},
    {"id": "A003", "voltage": 3.6}
]

for device in devices:
    if device["voltage"] > 3.1 and device["voltage"] < 3.5:
        print(device["id"] + " PASS")
    else:
        print(device["id"] + " FAIL")