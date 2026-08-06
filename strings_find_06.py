log = "DEVICE=SN001 TEST=POWER RESULT=FAIL ERROR=Voltage_High TIME=10.35s"

def extract_field(log, start_keyword, end_keyword):

    index_start = log.find(start_keyword)
    index_end = log.find(end_keyword)

    if index_start != -1 and index_end != -1:
        return log[
            index_start + len(start_keyword) : index_end 
            ].strip()

    return ""

result = {}

result["DEVICE"] = log[len("DEVICE="):log.find("TEST=")]

result["TEST"] = extract_field(log, "TEST=", "RESULT=")

result["RESULT"] = extract_field(log, "RESULT=", "ERROR=")

result["ERROR"] = extract_field(log, "ERROR=", "TIME=")

print(result)