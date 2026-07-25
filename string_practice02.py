# 以下是ChatGPT写的工程化的代码
logs = """
SN001 TEST=POWER RESULT=PASS
SN002 TEST=POWER RESULT=FAIL ERROR=Voltage_High
SN003 TEST=FLASH RESULT=FAIL ERROR=Write_Error
SN004 TEST=POWER RESULT=FAIL ERROR=Voltage_High
"""

total = 0
pass_count = 0
fail_count = 0
error_count = {}

for line in logs.split("\n"):

    if not line:
        continue

    total += 1

    result = {}

    for item in line.split():

        if "=" in item:
            key, value = item.split("=",1)
            result[key] = value

    if result.get("RESULT") == "PASS":
        pass_count += 1

    elif result.get("RESULT") == "FAIL":
        fail_count += 1

        error = result.get("ERROR")

        if error:
            error_count[error] = error_count.get(error,0)+1


print(total)
print(pass_count)
print(fail_count)
print(error_count)

# 以下是我自己写的代码
# logs = """
# SN001 TEST=POWER RESULT=PASS
# SN002 TEST=POWER RESULT=FAIL ERROR=Voltage_High
# SN003 TEST=FLASH RESULT=FAIL ERROR=Write_Error
# SN004 TEST=POWER RESULT=FAIL ERROR=Voltage_High
# """

# log_list = logs.split("\n")
# print(log_list)

# n_test = 0
# P_test = 0
# F_test = 0
# VH_fail = 0
# WE_fail = 0

# for log in log_list:
#     if log:
#         n_test += 1
#         strings = log.split()
#         results ={}
#         for string in strings:
#             if "=" in string:
#                 key, value = string.split("=")
#                 results[key] = value
#                 if value == "PASS":
#                     P_test += 1
#                 elif value == "FAIL":
#                     F_test +=1
#                 if key == "ERROR" and value == "Voltage_High":
#                     VH_fail += 1
#                 elif key == "ERROR" and value == "Write_Error":
#                     WE_fail += 1
#         log = results
#         #print(log)

# #print(log_list)

# print("总测试数量：", n_test)
# print("PASS数量:", P_test)
# print("FAIL数量:", F_test)
# print("失败原因统计:")

# print("Voltage_High:", VH_fail)
# print("Write_Error:", WE_fail)
      


# # 总测试数量: 4
# # PASS数量: 1
# # FAIL数量: 3

# # 失败原因统计:
# # Voltage_High: 2
# # Write_Error: 1
        

                      
                      