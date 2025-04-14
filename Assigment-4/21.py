# 21. Common Elements in Lists

a = [1, 2, 3]
b = [2, 3, 4]
common = []
for i in a:
    if i in b:
        common.append(i)
print(common)