log1 = "TEST=POWER"
log2 = "TEST=POWER VOLTAGE=220"
log3 = "TEST=POWER VOLTAGE=220V"
log4 = "TEST=POWER VOLTAGE="
log5 = "TEST=POWER VOLTAGE=abc"
log6 = "TEST=POWER VOLTAGE=199"
log7 = "TEST=POWER VOLTAGE=200"
log8 = "TEST=POWER VOLTAGE=220"
log9 = "TEST=POWER VOLTAGE=240"
log10 = "TEST=POWER VOLTAGE=241"

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

def create_data(status, voltage, message):
     data = {
          "status": status,
          "voltage": voltage,
          "message": message
     }
     return data

def check_voltage(log):
    try:
        results = parse_log(log, keywords)
        voltage = results["VOLTAGE"]
        if voltage == "":
            return create_data("FAIL", None, "电压数据为空")
        else:
            voltage = int(voltage)
            if voltage > 240 or voltage < 200:
                return create_data("FAIL", voltage, "电压异常")                
            else:
                return create_data("PASS", voltage, "电压正常")       
    except ValueError:
                return create_data("FAIL", None, "电压格式错误") 
    except KeyError:
                return create_data("FAIL", None, "没有电压数据")      
    except Exception:
                return create_data("FAIL", None, "出现其他日志解析错误")

result = check_voltage(log1)
print(result)
result = check_voltage(log2)
print(result)
result = check_voltage(log3)
print(result)
result = check_voltage(log4)
print(result)
result = check_voltage(log5)
print(result)
result = check_voltage(log6)
print(result)
result = check_voltage(log7)
print(result)
result = check_voltage(log8)
print(result)
result = check_voltage(log9)
print(result)
result = check_voltage(log10)
print(result)


