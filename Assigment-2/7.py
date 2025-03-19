
# 7. Factors of a number
num = int(input())
print("Factors:", end=" ")
i = 1
while i <= num:
    if num % i == 0:
        print(i, end=" ")
    i += 1
