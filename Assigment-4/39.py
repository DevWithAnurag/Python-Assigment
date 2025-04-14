# 39. Copy File Contents

f1 = open("sample.txt", "r")
f2 = open("copy.txt", "w")
for line in f1:
    f2.write(line)
f1.close()
f2.close()