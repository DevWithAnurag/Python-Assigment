# 38. Count Words and Lines in File
f = open("sample.txt", "r")
lines = f.readlines()
word_count = 0
for line in lines:
    word_count += len(line.split())
print("Lines:", len(lines))
print("Words:", word_count)
f.close()