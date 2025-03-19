# 25. Prime Factors of a number
num = int(input())
i = 2
print("Prime Factors:", end=" ")

while i * i <= num:
    while num % i == 0:
        print(i, end=" ")
        num //= i
    i += 1

if num > 1:
    print(num)
