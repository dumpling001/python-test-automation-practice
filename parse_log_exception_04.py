log1 = "TEST=POWER RESULT=FAIL ERROR=Voltage_High"
log2 = "TEST=POWER RESULT=FAIL"
log3 = "TEST=POWER ERROR=Voltage_High"
log4 = "RESULT=FAIL ERROR=Voltage_High"

keywords = ["TEST=", "RESULT=", "ERROR="]

# 代码重构：
# 不重复 find()，复用 keyword_position
# 不再用 i，直接 for keyword in keywords

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
    for keyword in keywords:
        if log.find(keyword) != -1:
            keyword_position[keyword] = log.find(keyword)


    for keyword in keywords:
        if keyword in keyword_position.keys():
            start_index = keyword_position[keyword]
            end_index = pick_next_position(keyword_position, keyword)
            if end_index is not None:
                value = log[start_index + len(keyword):end_index].strip()
            else:
                value = log[start_index + len(keyword):].strip()
            results[keyword.replace("=","")] = value
    return results

results1 = parse_log(log1, keywords)
results2 = parse_log(log2, keywords)
results3 = parse_log(log3, keywords)
results4 = parse_log(log4, keywords)
print(results1)
print(results2)
print(results3)
print(results4)