# 22. First 5 numbers divisible by 3 and 5
count, num = 0, 1
while count < 5:
    if num % 3 == 0 and num % 5 == 0:
        print(num, end=' ')
        count += 1
    num += 1