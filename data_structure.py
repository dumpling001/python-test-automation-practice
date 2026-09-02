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

def create_data(status, message, data=None):
    return {
            "status": status,
            "message": message,
            "data": data     
    }


def check_voltage(log):
    try:
        results = parse_log(log, keywords)
        voltage = results["VOLTAGE"]
        if voltage == "":
            return create_data("FAIL", "电压数据为空", {"voltage": None})
        else:
            voltage = int(voltage)
            if voltage > 240 or voltage < 200:
                return create_data("FAIL", "电压异常",  {"voltage": voltage})            
            else:
                return create_data("PASS", "电压正常",  {"voltage": voltage})
    except ValueError:
        return create_data("FAIL", "电压格式错误", {"voltage": None})
    except KeyError:
        return create_data("FAIL", "没有电压数据", {"voltage": None})
    except Exception:
        return create_data("FAIL", "出现其他日志解析错误", {"voltage": None})


def check_value(log, valuename, maxvalue, minvalue):
    results = parse_log(log, keywords)
    value = results[valuename]
    value = int(value)
    if value > maxvalue or value < minvalue:
        return create_data("FAIL", valuename+"异常", {valuename.lower(): value})
    else:
        return create_data("PASS", valuename+"正常", {valuename.lower(): value})

result = check_value(
    "TEST=POWER VOLTAGE=220",
    "VOLTAGE",
    240,
    200
)
print(result)

result = check_value(
    "TEST=POWER VOLTAGE=199",
    "VOLTAGE",
    240,
    200
)
print(result)



def generate_report(total, pass_count, fail_count, pass_percent, fail_percent, fail_datas):
    report = ""
    report += "========== 电压测试报告 ==========" + "\n" + "\n"
    report += "测试总数: " + str(total) + "\n" + "\n"
    report += "PASS数量: " + str(pass_count) + "\n"
    report += "FAIL数量: " + str(fail_count) + "\n" + "\n"
    report += "通过率: " + str(pass_percent) + "%" + "\n"
    report += "失败率: " + str(fail_percent) + "%"+ "\n" + "\n"
    report += "失败详情：" + "\n"
    fail_number = 0

    for data in fail_datas:
        fail_number += 1
        if data.get("data").get("voltage") is None:
            report += str(fail_number) + ". " + data.get("message") + "\n"
        else:
            report += str(fail_number) + ". " + data.get("message") + "(" + str(data.get("data").get("voltage") )+ ")"  + "\n"

    report += "\n" + "================================"
    return report

def save_report(report):  
    try:
        #with open("D:/Voltage_test_report.txt", "w") as f:
        with open("Voltage_test_report.txt", "w") as f:
            f.write(report)
            return create_data("PASS", "测试报告保存成功")
    except FileNotFoundError:
        return create_data("FAIL", "文件路径没找到")
    except TypeError:
        return create_data("FAIL", "报告数据类型错误")

def get_voltage(result):
    data = result.get("data")
    if data is None:
        return None
    
    return data.get("voltage")

# print(create_data("PASS", "保存成功"))
# print(create_data("PASS", "电压正常", 220))

# total = len(logs)
# fail_datas = []
# pass_count = 0
# fail_count = 0
# pass_percent = 0
# fail_percent = 0


# for log in logs:
#     #datas.append(check_voltage(log))
#     data = check_voltage(log)
#     if data["status"] == "PASS":
#         pass_count += 1
#     elif data["status"] == "FAIL":
#         fail_datas.append(data)
#         fail_count += 1

# if total !=0:
#     pass_percent = pass_count/total*100
#     fail_percent = fail_count/total*100


# report = generate_report(total, pass_count, fail_count, pass_percent, fail_percent, fail_datas)
# #save_report(123)
# #print("测试程序继续执行")
# result = save_report(report)
# if result["status"] == "PASS":
#     print("测试报告保存成功")
# elif result["status"] == "FAIL":
#     print("测试报告保存失败，但测试已经完成")
#     print(result["message"])
