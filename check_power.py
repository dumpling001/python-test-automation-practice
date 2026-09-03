log1 = "TEST=POWER VOLTAGE=220 CURRENT=5"
log2 = "TEST=POWER VOLTAGE=199 CURRENT=5"
log3 = "TEST=POWER VOLTAGE=220 CURRENT=0"
log4 = "TEST=POWER VOLTAGE=199 CURRENT=0"

def check_power(log):
    power_result = {}
    voltage_result = check_value(log, "VOLTAGE", 240, 200)
    current_result = check_value(log, "CURRENT", 10 , 1)
    power_result["message"] = voltage_result["message"] + "," + current_result["message"]
    power_result["data"] = voltage_result["data"] | current_result["data"]
    if voltage_result["status"] == "PASS" and current_result["status"] == "PASS":
        power_result["status"] = "PASS"
    else:
        power_result["status"] = "FAIL"
    return power_result