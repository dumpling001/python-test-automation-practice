# def check_voltage():
#     voltage = float(input())
#     if voltage >= 3.1 and voltage <=3.5:
#         print("PASS") 
#         return
#     else:
#         print("FAIL")
#         return
    
# check_voltage()

#修改后
def check_voltage(voltage):
    if float(voltage) >= 3.1 and float(voltage) <= 3.5:
        return "PASS"
    else:
        return "FAIL"
    
result = check_voltage(3.3)
print(result)
