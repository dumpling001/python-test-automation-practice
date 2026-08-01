log = "SN001 TEST=POWER RESULT=FAIL ERROR=Voltage_High TIME=10.35s"

# start = "ERROR="
# end = "TIME="

# start_p = log.find(start)
# end_p = log.find(end)


# #if start_p != -1:
# if start_p != -1 and end_p != -1:
#     #有的可能没有TIME=的字段
#     error_reason = log[start_p + len(start):end_p]
#     error_reason = error_reason.strip()
#     #以防有空格
#     print(error_reason)

start_keyword = "ERROR="
end_keyword = "TIME="

start_index = log.find(start_keyword)
end_index = log.find(end_keyword)

if start_index != -1 and end_index != -1:
    error_reason = log[
        start_index + len(start_keyword):end_index
    ].strip()

    print(error_reason)