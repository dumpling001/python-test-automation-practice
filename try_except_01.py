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

logs = [log1, log2, log3, log4, log5, log6, log7, log8, log9, log10]

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

total = len(logs)
fail_data = []
pass_count = 0
fail_count = 0
pass_percent = 0
fail_percent = 0


for log in logs:
    #datas.append(check_voltage(log))
    data = check_voltage(log)
    if data["status"] == "PASS":
        pass_count += 1
    elif data["status"] == "FAIL":
        fail_data.append(data)
        fail_count += 1

if total !=0:
    pass_percent = pass_count/total*100
    fail_percent = fail_count/total*100

print("总测试数: " + str(total))
print("PASS: " + str(pass_count))
print("FAIL: " + str(fail_count))
print("PASS百分比：" + str(pass_percent) + "%")
print("FAIL百分比：" + str(fail_percent) + "%")
