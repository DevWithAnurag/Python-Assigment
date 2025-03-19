# 7. Perfect Number Check
num = int(input())
total = 0
i = 1

while i < num:
    if num % i == 0:
        total += i
    i += 1

if total == num:
    print("Perfect Number")
else:
    print("Not Perfect")

