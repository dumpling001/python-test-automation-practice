log1 = "TEST=POWER"
log2 = "TEST=POWER VOLTAGE=220"
log3 = "TEST=POWER VOLTAGE=220V"
log4 = "TEST=POWER VOLTAGE="
log5 = "TEST=POWER VOLTAGE=abc"

keywords = ["TEST=", "RESULT=", "ERROR=", "VOLTAGE="]

def pick_next_position(keyword_position, keyword):
    next_positon = min(
        (position for position in keyword_position.values() if position > keyword_position[keyword]),
        default = None
        )
    return next_positon

def parse_log(log, keywords):
    keyword_position = {}
    results = {}
    #length = len(keywords)
    for keyword in keywords:
        position = log.find(keyword) 
        if position != -1:
            keyword_position[keyword] = position

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

def check_voltage(log):
    results = parse_log(log, keywords)
    try:
        voltage = int(results["VOLTAGE"])
        print(voltage, type(voltage))
    except ValueError:
        print("格式错误")
    except KeyError:
        print("没有电压数据")

check_voltage(log1)
check_voltage(log2)
check_voltage(log3)
check_voltage(log4)
check_voltage(log5)