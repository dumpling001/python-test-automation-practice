keywords = ["TEST=", "RESULT=", "ERROR="]

# 代码重构：
# 不重复 find()，复用 keyword_position
# 不再用 i，直接 for keyword in keywords

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

try:
    with open("Error_log.txt", "r", encoding="utf-8") as f:
        results = []
        for log in f:
            log = log.strip()
            if log:
                result = parse_log(log, keywords)
                results.append(result)
        count = len(results)
        print(results)
        

    fail_count = 0
    succ_count = 0
    for result in results:
        #print(result)
        if "RESULT" in result:
            if result["RESULT"] == "FAIL":
                fail_count += 1
            elif result["RESULT"] == "PASS":
                succ_count += 1

    print("总数："+str(count))
    print("FAIL:"+str(fail_count))
    print("PASS:"+str(succ_count))
    print("PASS比例："+str(succ_count/count*100 if count != 0 else 0)+"%")

except FileNotFoundError:
    print("文件不存在")