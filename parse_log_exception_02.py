#log = "TEST=POWER RESULT=FAIL ERROR=Voltage_High"
#log = "TEST=POWER RESULT=FAIL"
log = "TEST=POWER ERROR=Voltage_High"

keywords = ["TEST=", "RESULT=", "ERROR="]

length = len(keywords)
new_keywords_index = []

for i in range(length):
    #print(log.find(keywords[i]))
    if log.find(keywords[i]) != -1:
        new_keywords_index.append(log.find(keywords[i]))
        #print(new_keywords_index)
end_index = new_keywords_index[1]
print(end_index)