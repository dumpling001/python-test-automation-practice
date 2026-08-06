keywords = [
    "TEST=",
    "RESULT=",
    "ERROR=",
    "TIME="
]

# print(len(keywords))
for i in range(len(keywords)):
    if i != (len(keywords)-1):
        print("当前：" + keywords[i] + "   下一个:" + keywords[i+1])

# 当前：TEST=     下一个：RESULT=
# 当前：RESULT=   下一个：ERROR=
# 当前：ERROR=    下一个：TIME=