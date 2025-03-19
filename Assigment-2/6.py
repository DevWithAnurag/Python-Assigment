# 6. Prime Number Check
num = int(input())
if num < 2:
    print("Not Prime")
else:
    i = 2
    is_prime = True
    while i * i <= num:
        if num % i == 0:
            is_prime = False
            break
        i += 1
    print("Prime" if is_prime else "Not Prime")
