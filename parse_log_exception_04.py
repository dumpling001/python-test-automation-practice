log1 = "TEST=POWER RESULT=FAIL ERROR=Voltage_High"
log2 = "TEST=POWER RESULT=FAIL"
log3 = "TEST=POWER ERROR=Voltage_High"
log4 = "RESULT=FAIL ERROR=Voltage_High"

keywords = ["TEST=", "RESULT=", "ERROR="]
#keyword_position = {}
#length = len(keywords)
#results = {}

def pick_next_position(keyword_position, keyword):
    next_positon = min(
        (position for position in keyword_position.values() if position > keyword_position[keyword]),
        default = None
        )
    return next_positon

def parse_log(log, keywords):
    keyword_position = {}
    results = {}
    length = len(keywords)
    for i in range(length):
        if log.find(keywords[i]) != -1:
            key = keywords[i]
            value = log.find(keywords[i])

            keyword_position[key] = value
    #print(keyword_position)

    for i in range(length):
        start_index = log.find(keywords[i])
        #if log.find(keywords[i]) != -1:
        if start_index != -1:
            #start_index = log.find(keywords[i])
            end_index = pick_next_position(keyword_position, keywords[i])
            if end_index is not None:
                value = log[start_index + len(keywords[i]):end_index].strip()
            else:
                value = log[start_index + len(keywords[i]):].strip()
            results[keywords[i].replace("=","")] = value
    return results

results1 = parse_log(log1, keywords)
results2 = parse_log(log2, keywords)
results3 = parse_log(log3, keywords)
results4 = parse_log(log4, keywords)
print(results1)
print(results2)
print(results3)
print(results4)