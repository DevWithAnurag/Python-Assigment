# 40. Search Word in File

word = "hello"
f = open("sample.txt", "r")
line_num = 1
for line in f:
    if word in line:
        print("Found in line", line_num, ":", line.strip())
    line_num += 1
f.close()