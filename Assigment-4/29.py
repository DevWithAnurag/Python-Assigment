# 29. Repeated Elements in Tuple

t = (1, 2, 2, 3)
for i in t:
    if t.count(i) > 1:
        print(i)
        break