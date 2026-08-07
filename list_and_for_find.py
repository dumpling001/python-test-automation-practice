log = "TEST=POWER RESULT=FAIL ERROR=Voltage_High TIME=10.35s"

keywords = ["TEST=", "RESULT=", "ERROR=", "TIME="]

length = len(keywords)

result = {}

for i in range(length):

    if i != length - 1:

        start_index = log.find(keywords[i])
        end_index = log.find(keywords[i+1])

        start_len = len(keywords[i])

        result[keywords[i]] = log[start_index+start_len:end_index].strip()

for key, value in result.items():
    # print(key, value)
    print(key+value)
