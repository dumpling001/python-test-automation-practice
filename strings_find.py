log = "SN001 TEST=POWER RESULT=FAIL ERROR=Voltage_High"
# log = "SN002 TEST=POWER RESULT=PASS"

# if log.find("ERROR") > 1:
#     #print(log.find("ERROR"))
#     print("发现错误日志")
# else:
#     print("测试通过，没有错误信息")

position = log.find("ERROR")

if position != -1:
    print("发现错误日志")