log = "TEST=POWER RESULT=FAIL ERROR=Voltage_High TIME=10.35s"

key_words = ["TEST=", "RESULT=", "ERROR=", "TIME="]

#result = {}
new_result = {}

length = len(key_words)

for i in range(length):
    if i != length - 1:
        start_index = log.find(key_words[i])
        end_index = log.find(key_words[i+1])

        start_length = len(key_words[i])

        #result[key_words[i]] = log[start_index + start_length : end_index].strip()

        new_key = key_words[i].replace("=","")
        new_result[new_key] = log[start_index + start_length : end_index].strip()


print(new_result)
