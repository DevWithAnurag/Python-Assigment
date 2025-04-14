# 36. Read File Line by Line

f = open("sample.txt", "r")
for line in f:
    print(line.strip())
f.close()