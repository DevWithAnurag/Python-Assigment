# 17. Reverse List (Without Built-in)
lst = [1, 2, 3]
rev = []
for i in lst:
    rev = [i] + rev
print(rev)