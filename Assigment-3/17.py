# 17. Count digits in an integer
num = int(input())
count = 0

if num == 0:
    count = 1
else:
    while num > 0:
        count += 1
        num //= 10

print("Number of digits:", count)
