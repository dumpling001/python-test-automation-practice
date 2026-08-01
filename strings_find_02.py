log = "SN001 TEST=POWER RESULT=FAIL ERROR=Voltage_High"
#log = "SN001 TEST=POWER RESULT=FAIL"

# position = log.find("ERROR")
# #print(position)
# error_reason = log[int(position)-1:]
# print(error_reason)

# keyword = "ERROR="
# position = log.find(keyword)
# # error_reason = log[position+6 :]
# error_reason = log[position + len(keyword):]
# print(error_reason)

keyword = "ERROR="
position = log.find(keyword)
if position != -1:
# error_reason = log[position+6 :]
    error_reason = log[position + len(keyword):]
    print(error_reason)