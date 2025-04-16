# 19. Remove Negative Numbers
lst = [-1, 4, -5, 6]
pos = []
for i in lst:
    if i >= 0:
        pos.append(i)
print(pos)