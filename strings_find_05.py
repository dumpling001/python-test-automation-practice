log = "DEVICE=SN001 TEST=POWER RESULT=FAIL ERROR=Voltage_High TIME=10.35s"

keyword0 = "DEVICE"
keyword1 = "TEST"
keyword2 = "RESULT"
keyword3 = "ERROR"
keyword4 = "TIME"
#keywords = [keyword1, keyword2, keyword3, keyword4]
dict_log = {}

def extract_field(log, keyword_a, keyword_b):
    
    start_index_keyword_a = log.find(keyword_a)
    keyword_length = len(keyword_a)
    end_index_keyword_a = log.find(keyword_b)

    if start_index_keyword_a != -1 and end_index_keyword_a!= -1:
        result = log[(start_index_keyword_a + keyword_length + 1):(end_index_keyword_a - 1)]
        return result

dict_log[keyword0] = extract_field(log, keyword0, keyword1)
dict_log[keyword1] = extract_field(log, keyword1, keyword2)
dict_log[keyword2] = extract_field(log, keyword2, keyword3)
dict_log[keyword3] = extract_field(log, keyword3, keyword4)
print(dict_log)