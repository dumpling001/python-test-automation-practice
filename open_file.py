# f = open("Error_log.txt", "r", encoding="utf-8")
# content = f.read()
# print(content)
# f.close()

# with open("Error_log.txt", "r", encoding="utf-8") as f:
#     content = f.read()
#     print(content)
#     print(type(content))

#with open("Error_log.txt", "r", "encoding=utf-8") as f:
with open("Error_log.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())