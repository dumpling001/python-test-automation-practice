def generate_report(total, pass_count, fail_count, pass_percent, fail_percent, fail_datas):
    report = ""
    report += "========== 测试报告 ==========" + "\n" + "\n"
    report += "测试总数: " + str(total) + "\n" + "\n"
    report += "PASS数量: " + str(pass_count) + "\n"
    report += "FAIL数量: " + str(fail_count) + "\n" + "\n"
    report += "通过率: " + str(pass_percent) + "%" + "\n"
    report += "失败率: " + str(fail_percent) + "%"+ "\n" + "\n"
    report += "失败详情：" + "\n"
    fail_number = 0

    for data in fail_datas:
        fail_number += 1
        voltage = data.get("data").get("voltage")
        current = data.get("data").get("current")

        print(data.get("message"))
        print(voltage)
        print(current)

    report += "\n" + "================================"
    return report