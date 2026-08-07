result = {'TEST=': 'POWER', 'RESULT=': 'FAIL', 'ERROR=': 'Voltage_High'}

# for key in result:
#     new_key = key.replace("=","")
#     result[new_key] = result.pop(key)

# print(result)
new_result = {}

for key in result:
    new_key = key.replace("=","")
    new_result[new_key] = result[key]

print(new_result)