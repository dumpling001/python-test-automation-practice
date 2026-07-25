results = [
    {"case": "login_test", "status": "PASS"},
    {"case": "pay_test", "status": "FAIL"},
    {"case": "search_test", "status": "FAIL"}
]

n = 0

for result in results:
          if result["status"] == "FAIL":
                    print(result["case"]+" Failed")
                    n += 1

print("总共有"+str(n)+"个测试用例失败")
