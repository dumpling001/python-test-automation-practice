log = "SN001 TEST=POWER RESULT=FAIL ERROR=Voltage_High TIME=10.35s"

keyword0 = "DEVICE"
keyword1 = "TEST"
keyword2 = "RESULT"
keyword3 = "ERROR"
keyword4 = "TIME"
#keywords = [keyword1, keyword2, keyword3]
dict_log = {}

start_index_keyword0 = log.find(keyword0)
#keyword0_length = len(keyword0)
end_index_keyword0 = log.find(keyword1)

if end_index_keyword0!= -1:
    dict_log[keyword0] = log[:(end_index_keyword0 - 1)]
    print(dict_log)

start_index_keyword1 = log.find(keyword1)
keyword1_length = len(keyword1)
end_index_keyword1 = log.find(keyword2)

if start_index_keyword1 != -1 and end_index_keyword1!= -1:
    dict_log[keyword1] = log[(start_index_keyword1 + keyword1_length + 1):(end_index_keyword1 - 1)]
    print(dict_log)


start_index_keyword2 = log.find(keyword2)
keyword2_length = len(keyword2)
end_index_keyword2 = log.find(keyword3)

if start_index_keyword2 != -1 and end_index_keyword2!= -1:
    dict_log[keyword2] = log[(start_index_keyword2 + keyword2_length + 1):(end_index_keyword2 - 1)]
    print(dict_log)

start_index_keyword3 = log.find(keyword3)
keyword3_length = len(keyword3)
end_index_keyword3 = log.find(keyword4)

if start_index_keyword3 != -1 and end_index_keyword3!= -1:
    dict_log[keyword3] = log[(start_index_keyword3 + keyword3_length + 1):(end_index_keyword3 - 1)]
    print(dict_log)
# {
#     "DEVICE": "SN001",
#     "TEST": "POWER",
#     "RESULT": "FAIL",
#     "ERROR": "Voltage_High"
# }