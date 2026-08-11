log = "TEST=POWER ERROR=Voltage_High"

keywords = ["TEST=", "RESULT=", "ERROR="]

keyword_position = {}

length = len(keywords)
results = {}

for i in range(length):
    if log.find(keywords[i]) != -1:
        key = keywords[i]
        value = log.find(keywords[i])

        keyword_position[key] = value
print(keyword_position)

def pick_next_position(keyword_position, keyword):
    next_positon = min(
        (position for position in keyword_position.values() if position > keyword_position[keyword]),
        default = None
        )
    return next_positon

for i in range(length):
    if log.find(keywords[i]) != -1:
        start_index = log.find(keywords[i])
        end_index = pick_next_position(keyword_position, keywords[i])
        value = log[start_index + len(keywords[i]):end_index].strip()
        results[keywords[i].replace("=","")] = value

print(results)