#log = "TEST=POWER RESULT=FAIL ERROR=Voltage_High"
log = "TEST=POWER RESULT=FAIL"
#log = "TEST=POWER ERROR=Voltage_High"

keywords = ["TEST=", "RESULT=", "ERROR="]

def parse_log(log, keywords):
    result = {}
    length = len(keywords)

    for i in range(length):
        #print(i)
        if log.find(keywords[i]) != -1:
            length_start = len(keywords[i])
            start_index = log.find(keywords[i])           
            key = keywords[i].replace("=", "")
            if i+1 == length or log.find(keywords[i+1]) == -1:
                end_index = len(log)
                result[key] = log[start_index + length_start : end_index].strip()                 
            else:
                end_index = log.find(keywords[i+1])
                result[key] = log[start_index + length_start : end_index].strip() 

    return result

result = parse_log(log, keywords)
print(result)