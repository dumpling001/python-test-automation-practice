log = "2026-07-23 10:25:36 DEVICE=SN001 TEST=POWER RESULT=FAIL ERROR=Voltage_High"

strings = log.split()
#print(strings)
#['2026-07-23', '10:25:36', 'DEVICE=SN001', 'TEST=POWER', 'RESULT=FAIL', 'ERROR=Voltage_High']
# for item in strings:
#     key, value = item.split("=") if "=" in item else ("","")
#     if key == "DEVICE":
#         print("设备编号：",value)
#     elif key == "TEST":
#         print("测试项目：",value)
#     elif key == "RESULT":
#         print("测试结果：",value)

results = {}
for item in strings:
    if "=" in item:
        key,value = item.split("=")
        results[key] = value
print(results)