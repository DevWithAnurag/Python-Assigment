# 20. Skip multiples of 5
i = 1
result = []

while i <= 20:
    if i % 5 != 0:
        result.append(i)
    i += 1

print(result)

