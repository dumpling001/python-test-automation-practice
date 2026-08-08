log = "TEST=POWER RESULT=FAIL ERROR=Voltage_High TIME=10.35s"


def parse_log(log):
    key_words = ["TEST=", "RESULT=", "ERROR=", "TIME="]

    #result = {}
    result = {}

    length = len(key_words)

    for i in range(length):
        if i != length - 1:
            start_index = log.find(key_words[i])
            end_index = log.find(key_words[i+1])

            start_length = len(key_words[i])

            #result[key_words[i]] = log[start_index + start_length : end_index].strip()

            key = key_words[i].replace("=","")
            result[key] = log[start_index + start_length : end_index].strip()

    return result


result = parse_log(log)
print(result)